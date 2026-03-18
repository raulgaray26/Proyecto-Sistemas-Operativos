from threading import Thread, Semaphore, Lock
import time
import bitacora

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
        bitacora.log_inicio_simulacion(self.capacidad)

        for hilo in self.cola_espera:
            hilo.start()

        for hilo in self.cola_espera:
            hilo.join()

        print("\nLaboratorio cerrado.\n")
        self._mostrar_resumen()
        bitacora.log_fin_simulacion(self.capacidad, self.computadoras_disponibles)

    def usar_computadora(self, id_estudiante, nombre, tarea, tiempo_uso):
        print(f"[{id_estudiante}] {nombre} está esperando una computadora...")
        bitacora.log_estudiante_esperando(id_estudiante, nombre)

        # ── El hilo se bloquea aquí si no hay computadoras disponibles ──
        self.supervisor.acquire()

        try:
            # ── Sección crítica: modificar estado compartido ──
            self.mutex.acquire()
            bitacora.log_mutex_adquirido(id_estudiante, nombre, "Asignando computadora")

            self.computadoras_disponibles -= 1
            numero_pc = self._asignar_computadora()
            self.registro_uso[numero_pc] = {
                "id_estudiante" : id_estudiante,
                "nombre"        : nombre,
                "tarea"         : tarea,
                "inicio"        : time.strftime("%H:%M:%S")
            }

            print(f"[{id_estudiante}] {nombre} → PC {numero_pc} | Tarea: '{tarea}' | Tiempo: {tiempo_uso}s | Disponibles: {self.computadoras_disponibles}/{self.capacidad}")
            bitacora.log_semaforo_adquirido(id_estudiante, nombre, numero_pc, tarea, tiempo_uso,
                                            self.computadoras_disponibles, self.capacidad)

            self.mutex.release()
            bitacora.log_mutex_liberado(id_estudiante, nombre, "Computadora asignada, saliendo de sección crítica")
            # ── Fin sección crítica ──

            time.sleep(tiempo_uso)

            # ── Sección crítica: liberar recurso ──
            self.mutex.acquire()
            bitacora.log_mutex_adquirido(id_estudiante, nombre, "Liberando computadora")

            del self.registro_uso[numero_pc]
            self.computadoras_disponibles += 1

            print(f"[{id_estudiante}] {nombre} terminó '{tarea}' en PC {numero_pc} | Disponibles: {self.computadoras_disponibles}/{self.capacidad}")
            bitacora.log_estudiante_termino(id_estudiante, nombre, tarea, numero_pc,
                                            self.computadoras_disponibles, self.capacidad)

            self.mutex.release()
            bitacora.log_mutex_liberado(id_estudiante, nombre, "Computadora liberada, saliendo de sección crítica")
            # ── Fin sección crítica ──

        finally:
            self.supervisor.release()
            bitacora.log_semaforo_liberado(id_estudiante, nombre)

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
