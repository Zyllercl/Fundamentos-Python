# --------------------------
# Creación de la Clase
# --------------------------
class Libro:
    # --------------------------
    # Constructor
    # --------------------------
    def __init__(self, titulo, autor, genero):
        # --------------------------
        # Atributos de Instancia [Variables Protegidas]
        # --------------------------
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    # --------------------------
    # Métodos GET
    # --------------------------
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor
    
    @property
    def genero(self):
        return self._genero