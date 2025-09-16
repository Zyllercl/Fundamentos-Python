"""
Ejercicio de Herencia Multiple en Python
========================================
En este script se aplicará la Herencia Múltiple ya que la Clase 'Rectangulo' heredará de FiguraGeometrica y Color
"""

from figura_geometrica import FiguraGeometrica
from color import Color

# -----------------------------
# Creación de Clase
# -----------------------------
class Rectangulo(Color, FiguraGeometrica):
    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(self, color, ancho, alto):
        # Inicilización de los Objetos de la Clase Padre con Herencia Múltiple
        Color.__init__(self, color)
        FiguraGeometrica.__init__(self, ancho, alto)
        

    # -----------------------------
    # Método para Calcular Área
    # -----------------------------
    def calcular_area(self):
        # Se accede a los atributos de la Clase Padre de Figura Geometrica
        area_rectangulo = self.alto * self.ancho

        return area_rectangulo
    
    def __str__(self):
        # Llamada a la Clases Padres __str__ de Color y FiguraGeometrica respectivamente
        return f'''
Método __str__: {Color.__str__(self)}
Método __str__: {FiguraGeometrica.__str__(self)}
'''