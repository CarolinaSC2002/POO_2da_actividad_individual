from .local import Local

class Oficina(Local):
    valor_area = 3500000.0

    def __init__(self, identificador: int, area: int, direccion: str,
                 tipo_local: str, es_gobierno: bool):
        super().__init__(identificador, area, direccion, tipo_local)
        self._es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self._es_gobierno}")
