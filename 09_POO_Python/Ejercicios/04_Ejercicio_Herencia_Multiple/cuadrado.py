"""
Ejercicio de Herencia Multiple en Python
========================================
En este script se aplicará la Herencia Múltiple ya que la Clase 'Cuadrado' heredará de FiguraGeometrica y Color
"""
from figura_geometrica import FiguraGeometrica
from color import Color

# -----------------------------
# Creación de Clase
# -----------------------------
class Cuadrado(FiguraGeometrica, Color):
    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(self, lado, color):
        # Inicilización de los Objetos de la Clase Padre con Herencia Múltiple
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    # -----------------------------
    # Método para Calcular Área
    # -----------------------------
    def calcular_area(self):
        # Se accede a los atributos de la Clase Padre de Figura Geometrica
        area_cuadrado = self.alto * self.ancho

        return area_cuadrado

    def __str__(self):
        # Llamada a la Clases Padres __str__ de FiguraGeometrica y Color respectivamente
        return f'''
Método __str__: {FiguraGeometrica.__str__(self)}
Método __str__: {Color.__str__(self)}
'''