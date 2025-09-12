
# -----------------------------
# Creación de la Clase
# -----------------------------
class Color:
    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(self, color):
        self._color = color
    
    # -----------------------------
    # Métodos SET y GET
    # -----------------------------
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color
        return self._color

    def __str__(self):
        return f'[Color] Color: {self._color}'