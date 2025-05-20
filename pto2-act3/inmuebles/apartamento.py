from .inmueble_vivienda import InmuebleVivienda

class Apartamento(InmuebleVivienda):
    def __init__(self, identificador: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int):
        super().__init__(identificador, area, direccion,
                         numero_habitaciones, numero_banos)

    def imprimir(self):
        super().imprimir()
