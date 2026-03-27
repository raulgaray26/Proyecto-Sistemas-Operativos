import time
import info_estudiantes
import info_proyecto
import bitacora
from estudiante import Estudiante
from laboratorio import Laboratorio
 
def main():
    print("--- Menú Principal ---")
    print("1. Ver nombres de estudiantes")
    print("2. Ver descripción del proyecto")
    print("3. Ejecutar simulación del laboratorio")
    print("4. Salir")
    
    opcion = 0
    while opcion != 4:
        opcion = input("Seleccione una opción: ")
 
        if opcion == "1":
            info_estudiantes.nombres_estudiantes()
 
        elif opcion == "2":
            info_proyecto.descripcion_proyecto()
 
        elif opcion == "3":
            # Inicializar la bitácora antes de arrancar la simulación
            bitacora.configurar_bitacora()
 
            CAPACIDAD = 3
            laboratorio = Laboratorio(CAPACIDAD)
 
            estudiantes = [
                Estudiante(1,  "Leonor",     "Investigar en internet"),
                Estudiante(2,  "Raul",       "Hacer tarea de Python"),
                Estudiante(3,  "Andrea",     "Usar Word"),
                Estudiante(4,  "Carlos",     "Preparar exposición"),
                Estudiante(5,  "María",      "Revisar correo institucional"),
                Estudiante(6,  "Karel",      "Escribir un correo a Wong"),
                Estudiante(7,  "Juan Diego", "Instalar Linux"),
                Estudiante(8,  "Sebastian",  "Collage de photodumps"),
                Estudiante(9,  "Daniel",     "Stremear en Youtube"),
                Estudiante(10, "Justin",     "Jugar Genshin"),
            ]
 
            print()
            print("=" * 55)
            print("       ESTADO INICIAL DEL LABORATORIO")
            print("=" * 55)
            print(f"  Computadoras disponibles : {CAPACIDAD}/{CAPACIDAD}")
            print(f"  Estudiantes en cola      : {len(estudiantes)}")
            print("-" * 55)
            print("  Cola de espera:")
            for est in estudiantes:
                print(f"    [{est.id_estudiante:02d}] {est.nombre:<15} → {est.tarea}")
            print("=" * 55)
            print()
 
            time.sleep(1)
 
            laboratorio.recibir_estudiantes(estudiantes)
            laboratorio.abrir()
 
        elif opcion == "4":
            print("Saliendo del programa.")
            break
 
        else:
            print("Opción no válida.")
 
 
if __name__ == "__main__":
    main()