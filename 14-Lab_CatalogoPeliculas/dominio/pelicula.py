
class Pelicula:
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        
    def __str__(self) -> str:
        return f'Pelicula: {self._nombre}'
    
    # Metodo GET
    @property
    def get_nombre(self):
        self._nombre
    
    # Metodo SET
    @get_nombre.setter
    def set_nombre(self, nombre):
        self._nombre = nombre