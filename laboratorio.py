from threading import Thread, Semaphore, Lock
import time

class Laboratorio:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.supervisor = Semaphore(capacidad)
        self.mutex = Lock()
        self.computadoras_disponibles = capacidad
        self.registro_uso = {}
        self.cola_espera = []

    def recibir_estudiantes(self, estudiantes):
        for i in range(len(estudiantes)):
            id_estudiante = estudiantes[i].id_estudiante
            nombre        = estudiantes[i].nombre
            tarea         = estudiantes[i].tarea
            tiempo_uso    = estudiantes[i].tiempo_uso

            hilo = Thread(target=self.usar_computadora, args=(id_estudiante, nombre, tarea, tiempo_uso))
            self.cola_espera.append(hilo)

    def abrir(self):
        print("\nLaboratorio abierto.\n")

        for hilo in self.cola_espera:
            hilo.start()

        for hilo in self.cola_espera:
            hilo.join()

        print("\nLaboratorio cerrado.\n")
        self._mostrar_resumen()

    def usar_computadora(self, id_estudiante, nombre, tarea, tiempo_uso):
        print(f"[{id_estudiante}] {nombre} está esperando una computadora...")

        self.supervisor.acquire()

        try:
            self.mutex.acquire()

            self.computadoras_disponibles -= 1
            numero_pc = self._asignar_computadora()
            self.registro_uso[numero_pc] = {
                "id_estudiante" : id_estudiante,
                "nombre"        : nombre,
                "tarea"         : tarea,
                "inicio"        : time.strftime("%H:%M:%S")
            }

            print(f"[{id_estudiante}] {nombre} → PC {numero_pc} | Tarea: '{tarea}' | Tiempo: {tiempo_uso}s | Disponibles: {self.computadoras_disponibles}/{self.capacidad}")

            self.mutex.release()

            time.sleep(tiempo_uso)

            self.mutex.acquire()

            del self.registro_uso[numero_pc]
            self.computadoras_disponibles += 1

            print(f"[{id_estudiante}] {nombre} terminó '{tarea}' en PC {numero_pc} | Disponibles: {self.computadoras_disponibles}/{self.capacidad}")

            self.mutex.release()

        finally:
            self.supervisor.release()

    def _asignar_computadora(self):
        for numero in range(1, self.capacidad + 1):
            if numero not in self.registro_uso:
                return numero

    def _mostrar_resumen(self):
        print("=" * 55)
        print("         RESUMEN DE SESIÓN DEL LABORATORIO")
        print("=" * 55)
        print(f"  Computadoras totales : {self.capacidad}")
        print(f"  Computadoras libres  : {self.computadoras_disponibles}")
        print(f"  Sesiones en curso    : {len(self.registro_uso)}")
        print("=" * 55)