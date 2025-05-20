from .inmueble import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, identificador: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int):
        super().__init__(identificador, area, direccion)
        self._numero_habitaciones = numero_habitaciones
        self._numero_banos = numero_banos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self._numero_habitaciones}")
        print(f"Número de baños = {self._numero_banos}")
