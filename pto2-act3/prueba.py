from inmuebles.apartamento_familiar import ApartamentoFamiliar
from inmuebles.apartaestudio import Apartaestudio

def main():
    # Prueba Apartamento Familiar
    print("Datos apartamento familiar")
    apto_fam = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    apto_fam.calcular_precio_venta(ApartamentoFamiliar.valor_area)
    apto_fam.imprimir()
    print()

    # Prueba Apartaestudio
    print("Datos apartaestudio")
    apt_est = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
    apt_est.calcular_precio_venta(Apartaestudio.valor_area)
    apt_est.imprimir()

if __name__ == "__main__":
    main()
