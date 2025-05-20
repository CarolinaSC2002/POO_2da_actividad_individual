from .local import Local

class LocalComercial(Local):
    valor_area = 3000000.0

    def __init__(self, identificador: int, area: int, direccion: str,
                 tipo_local: str, centro_comercial: str):
        super().__init__(identificador, area, direccion, tipo_local)
        self._centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self._centro_comercial}")
