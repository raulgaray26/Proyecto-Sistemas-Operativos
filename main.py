import info_estudiantes
import info_proyecto
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
            laboratorio = Laboratorio(3)

            estudiantes = [
                Estudiante(1, "Leonor", "Investigar en internet"),
                Estudiante(2, "Raul", "Hacer tarea de Python"),
                Estudiante(3, "Andrea", "Usar Word"),
                Estudiante(4, "Carlos", "Preparar exposición"),
                Estudiante(5, "María", "Revisar correo institucional")
            ]

            laboratorio.recibir_estudiantes(estudiantes)
            laboratorio.abrir()

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()