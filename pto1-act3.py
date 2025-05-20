class Cuenta:
    def __init__(self, saldo=0.0, tasa_anual=0.0):
        self._saldo = saldo
        self._numero_consignaciones = 0
        self._numero_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0.0

    def consignar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            self._numero_consignaciones += 1

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            self._numero_retiros += 1
            return True
        return False

    def calcular_interes(self):
        interes_mensual = (self._tasa_anual / 12) * self._saldo
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes()

    def imprimir(self):
        print(f"Saldo = $ {self._saldo:.3f}")
        print(f"Comisión mensual = $ {self._comision_mensual}")
        print(f"Número de transacciones = {self._numero_consignaciones + self._numero_retiros}")


class CuentaAhorros(Cuenta):
    def __init__(self, saldo=0.0, tasa_anual=0.0):
        super().__init__(saldo, tasa_anual)
        self._activa = saldo >= 10000

    def consignar(self, cantidad):
        if self._activa:
            super().consignar(cantidad)
        self._activa = self._saldo >= 10000

    def retirar(self, cantidad):
        if self._activa:
            if super().retirar(cantidad):
                pass
        self._activa = self._saldo >= 10000

    def extracto_mensual(self):
        transacciones = self._numero_consignaciones + self._numero_retiros
        if transacciones > 4:
            self._comision_mensual = 1000 * (transacciones - 4)
        super().extracto_mensual()
        self._activa = self._saldo >= 10000


def prueba_cuenta_interactiva():
    print("Cuenta de ahorros")

    saldo_inicial_str = input("Ingrese saldo inicial=$\n")
    print(saldo_inicial_str)
    saldo_inicial = float(saldo_inicial_str)

    tasa_str = input("Ingrese tasa de interés= ").replace(',', '.')
    print("Ingrese tasa de interés=", tasa_str)
    tasa_anual = float(tasa_str)

    cuenta = CuentaAhorros(saldo_inicial, tasa_anual)

    cantidad_consignar_str = input("Ingresar cantidad a consignar: $\n")
    print("Ingresar cantidad a consignar: $", cantidad_consignar_str)
    cantidad_consignar = float(cantidad_consignar_str)
    cuenta.consignar(cantidad_consignar)

    cantidad_retirar_str = input("Ingresar cantidad a retirar: $\n")
    print("Ingresar cantidad a retirar: $", cantidad_retirar_str)
    cantidad_retirar = float(cantidad_retirar_str)
    cuenta.retirar(cantidad_retirar)

    cuenta.extracto_mensual()
    cuenta.imprimir()


# Ejecutar la prueba interactiva
prueba_cuenta_interactiva()
