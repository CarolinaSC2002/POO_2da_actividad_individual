from .casa_urbana import CasaUrbana

class CasaConjuntoCerrado(CasaUrbana):
    valor_area = 2500000.0

    def __init__(self, identificador: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int,
                 valor_administracion: int, tiene_piscina: bool, tiene_campos_deportivos: bool):
        super().__init__(identificador, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self._valor_administracion = valor_administracion
        self._tiene_piscina = tiene_piscina
        self._tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administracion}")
        print(f"Tiene piscina? = {self._tiene_piscina}")
        print(f"Tiene campos deportivos? = {self._tiene_campos_deportivos}")
