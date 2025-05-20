from .apartamento import Apartamento

class Apartaestudio(Apartamento):
    valor_area = 1500000.0

    def __init__(self, identificador: int, area: int, direccion: str):
        # Apartaestudio: 1 habitación, 1 baño
        super().__init__(identificador, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()
