class Inmueble:
    def __init__(self, identificador: int, area: int, direccion: str):
        self._identificador = identificador
        self._area = area
        self._direccion = direccion
        self._precio_venta = 0.0

    def calcular_precio_venta(self, valor_area: float) -> float:
        self._precio_venta = self._area * valor_area
        return self._precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self._identificador}")
        print(f"Area = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = ${self._precio_venta:.2f}")
