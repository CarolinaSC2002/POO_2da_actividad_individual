from universidad.estudiante import Estudiante
from universidad.profesor import Profesor

if __name__ == "__main__":
    # Crear una instancia de Estudiante
    estudiante1 = Estudiante("Ana Pérez", "Calle 123", "Ingeniería de Sistemas", 4)

    # Crear una instancia de Profesor
    profesor1 = Profesor("Carlos López", "Avenida 456", "Ciencias de la Computación", "Titular")

    # Acceder a la información
    print("--- Estudiante ---")
    print(f"Nombre: {estudiante1.get_nombre()}")
    print(f"Carrera: {estudiante1.get_carrera()}")
    print(f"Semestre: {estudiante1.get_semestre()}")
    print(f"Dirección: {estudiante1.get_direccion()}")

    print("\n--- Profesor ---")
    print(f"Nombre: {profesor1.get_nombre()}")
    print(f"Departamento: {profesor1.get_departamento()}")
    print(f"Categoría: {profesor1.get_categoria()}")
    print(f"Dirección: {profesor1.get_direccion()}")

    # Modificar información del estudiante
    estudiante1.set_semestre(5)
    print(f"\n--- Estudiante (Semestre Actualizado) ---")
    print(f"Nombre: {estudiante1.get_nombre()}, Semestre: {estudiante1.get_semestre()}")