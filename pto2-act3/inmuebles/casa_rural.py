from .casa import Casa

class CasaRural(Casa):
    valor_area = 1500000.0

    def __init__(self, identificador: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int,
                 numero_pisos: int, distancia_cabecera: int, altitud: int):
        super().__init__(identificador, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self._distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar = {self._altitud} metros")
