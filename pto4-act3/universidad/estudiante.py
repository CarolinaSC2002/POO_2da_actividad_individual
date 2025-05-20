from .persona import Persona  # Importa la clase Persona desde el mismo paquete

class Estudiante(Persona):
    def __init__(self, nombre, direccion, carrera, semestre):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def get_carrera(self):
        return self.carrera

    def get_semestre(self):
        return self.semestre

    def set_carrera(self, carrera):
        self.carrera = carrera

    def set_semestre(self, semestre):
        self.semestre = semestre