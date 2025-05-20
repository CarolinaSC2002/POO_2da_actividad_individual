from .apartamento import Apartamento

class ApartamentoFamiliar(Apartamento):
    valor_area = 2000000.0

    def __init__(self, identificador: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, valor_administracion: int):
        super().__init__(identificador, area, direccion,
                         numero_habitaciones, numero_banos)
        self._valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administracion}")
