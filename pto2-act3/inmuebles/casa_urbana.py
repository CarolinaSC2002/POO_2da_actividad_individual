from .casa import Casa

class CasaUrbana(Casa):
    def __init__(self, identificador: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):
        super().imprimir()
