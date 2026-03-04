import info_estudiantes
import info_proyecto

def main():
    print("--- Menú Principal ---")
    print("1. Ver nombres de estudiantes")
    print("2. Ver descripción del proyecto")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        info_estudiantes.nombres_estudiantes()
    elif opcion == "2":
        info_proyecto.descripcion_proyecto()
    else:
        print("Opción no válida.")
    

if __name__ == "__main__":
    main()