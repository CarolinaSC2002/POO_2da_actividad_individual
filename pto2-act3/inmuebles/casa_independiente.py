from .casa_urbana import CasaUrbana

class CasaIndependiente(CasaUrbana):
    valor_area = 3000000.0

    def __init__(self, identificador: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):
        super().imprimir()
