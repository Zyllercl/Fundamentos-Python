# -------------------------------
# Creación de la clase Pelicula
# -------------------------------
class Pelicula:
    # Constructor
    def __init__(self, nombre):
        self._nombre = nombre
    
    # Método __str__ modificado para mostrar el nombre de la película
    def __str__(self):
        return f'Nombre película: {self._nombre}'

    # Método GET
    @property
    def nombre(self):
        return self._nombre
    
    # Método SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

