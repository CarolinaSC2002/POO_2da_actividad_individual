from .inmueble_vivienda import InmuebleVivienda

class Casa(InmuebleVivienda):
    def __init__(self, identificador: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador, area, direccion,
                         numero_habitaciones, numero_banos)
        self._numero_pisos = numero_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self._numero_pisos}")
