# main.py

from mi_clase import MiClase, alumno, nombre, apellido_materno, apellido_paterno, no_control, semestre


def main():
    persona = MiClase("Juan")
    print(persona.saludar())

if __name__ == "__main__":
    main()


def main():
    # Crear un diccionario para almacenar los alumnos
    alumnos_dict = {}

    # Capturar 3 alumnos desde teclado
    for i in range(1, 4):
        print(f"\nCapturando datos del alumno {i}:")

        nombre = input("Ingresa el nombre: ")
        apellido_paterno = input("Ingresa el apellido paterno: ")
        apellido_materno = input("Ingresa el apellido materno: ")
        no_control = input("Ingresa el número de control: ")
        semestre = int(input("Ingresa el semestre: "))

        # Crear una nueva instancia de Alumno y asignar los valores
        alumno = Alumno()
        alumno.set_nombre(nombre)
        alumno.set_apellido_paterno(apellido_paterno)
        alumno.set_apellido_materno(apellido_materno)
        alumno.set_no_control(no_control)
        alumno.set_semestre(semestre)

        # Almacenar el alumno en el diccionario usando el no. de control como clave
        alumnos_dict[alumno.get_no_control()] = alumno

    # Mostrar la lista de alumnos capturados
    print("\nLista de alumnos capturados:")
    for no_control, alumno in alumnos_dict.items():
        print(f"\nNo. de Control: {no_control}")
        print(f"Nombre Completo: {alumno.get_nombre()} {alumno.get_apellido_paterno()} {alumno.get_apellido_materno()}")
        print(f"Semestre: {alumno.get_semestre()}")


# Ejecutar la función principal
if __name__ == "__main__":
    main()