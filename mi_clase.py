# mi_clase.py

class MiClase:
    def __init__(self, nombre):
        self.__nombre = nombre

    def saludar(self):
        return f"Hola, {self.__nombre}!"


class Alumno:
    def __init__(self):
        # Atributos privados inicializados en None
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para asignar valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre


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

# Ejemplo de cómo mostrar los alumnos capturados
print("\nLista de alumnos capturados:")
for no_control, alumno in alumnos_dict.items():
    print(f"\nNo. de Control: {no_control}")
    print(f"Nombre Completo: {alumno.get_nombre()} {alumno.get_apellido_paterno()} {alumno.get_apellido_materno()}")
    print(f"Semestre: {alumno.get_semestre()}")
