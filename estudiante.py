import random

class Estudiante:

    def __init__(self, id_estudiante, nombre, tarea):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.tarea = tarea
        self.tiempo_uso = random.randint(1, 20) #De esta manera probamos el tiempo de los estudiantes
        self.computadora_asignada = None

    def __str__(self):
        return f"Estudiante({self.id_estudiante}, {self.nombre}, {self.tarea}, {self.tiempo_uso}s)"