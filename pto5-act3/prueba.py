from profesores.profesor_titular import ProfesorTitular
from profesores.profesor import Profesor

def main():
    """
    Método main que crea un Profesor pero instanciando la clase
    ProfesorTitular. ¿Qué se imprimirá en pantalla?
    """
    profesor1: Profesor = ProfesorTitular()
    profesor1.imprimir()

if __name__ == "__main__":
    main()
