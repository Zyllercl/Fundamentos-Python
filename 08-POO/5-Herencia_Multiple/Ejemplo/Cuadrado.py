from FiguraGeometrica import FiguraGeometrica
from Color import Color

# Clase Hija
class Cuadrado(FiguraGeometrica, Color):
    # Inicializacion de clase hija
    def __init__(self, lado, color):
        # Inicializacion de la clase Padre
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return self._alto * self._alto
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}' 