from .inmueble import Inmueble

class Local(Inmueble):
    class Tipo:
        INTERNO = 'INTERNO'
        CALLE = 'CALLE'

    def __init__(self, identificador: int, area: int, direccion: str, tipo_local: str):
        super().__init__(identificador, area, direccion)
        self._tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self._tipo_local}")
