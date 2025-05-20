from profesores.profesor import Profesor

class ProfesorTitular(Profesor):
    """
    Esta clase denominada ProfesorTitular es una subclase de Profesor.
    """

    def imprimir(self):
        """
        Método que sobreescribe el método imprimir heredado de la clase
        padre Profesor.
        """
        print("Es un profesor titular.")
