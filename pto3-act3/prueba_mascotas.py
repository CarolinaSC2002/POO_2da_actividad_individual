from TiendaMascotas.perro_pequenio import Schnauzer, Caniche
from TiendaMascotas.perro_mediano import Bulldog
from TiendaMascotas.perro_grande import PastorAleman
from TiendaMascotas.gato_sin_pelo import Esfinge
from TiendaMascotas.gato_pelo_largo import Angora
from TiendaMascotas.gato_pelo_corto import AzulRuso


def main():
    # Crear perros
    p1 = Schnauzer("Max", 3, "gris", 6.0, True)
    p2 = Bulldog("Bruno", 4, "blanco", 18.0, False)
    p3 = PastorAleman("Thor", 5, "negro", 30.0, True)

    # Crear gatos
    g1 = Esfinge("Luna", 2, "rosado", 1.2, 1.5)
    g2 = Angora("Michi", 3, "blanco", 1.0, 1.3)
    g3 = AzulRuso("Nube", 1, "gris", 0.8, 1.0)

    # Imprimir información
    print(f"{p1.__class__.__name__}: {p1.nombre}, {p1.edad} años, {p1.color}, {p1.peso} kg, muerde={p1.muerde}")
    print(f"{p2.__class__.__name__}: {p2.nombre}, {p2.edad} años, {p2.color}, {p2.peso} kg, muerde={p2.muerde}")
    print(f"{p3.__class__.__name__}: {p3.nombre}, {p3.edad} años, {p3.color}, {p3.peso} kg, muerde={p3.muerde}")
    print(f"{g1.__class__.__name__}: {g1.nombre}, {g1.edad} años, {g1.color}, salta {g1.altura_salto}m x {g1.longitud_salto}m")
    print(f"{g2.__class__.__name__}: {g2.nombre}, {g2.edad} años, {g2.color}, salta {g2.altura_salto}m x {g2.longitud_salto}m")
    print(f"{g3.__class__.__name__}: {g3.nombre}, {g3.edad} años, {g3.color}, salta {g3.altura_salto}m x {g3.longitud_salto}m")

    # Usar método estático
    Schnauzer.sonido()
    Esfinge.sonido()


if __name__ == "__main__":
    main()
