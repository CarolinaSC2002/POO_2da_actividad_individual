class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_direccion(self, direccion):
        self.direccion = direccion