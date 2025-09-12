"""
Ejercicio de Herencia Multiple en Python
========================================
Este script muestra un ejemplo de como abordar la Herencia Multiple, para ello en este archivo se creará la Clase Padre y posteriormente se crearan las Clases Hijas que tomaran los atributos y método de la Clase Padre
"""

# -----------------------------
# Creación de la Clase
# -----------------------------
class FiguraGeometrica:
    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(self, ancho, alto):
        # -----------------------------
        # Atributos de Instancia
        # -----------------------------
        if self._validar_valor(ancho):
            self._ancho = ancho     # Variable Privada
        else:
            self._ancho = 0
            print(f'[ERROR] Valor erroneo del ancho: {ancho}')

        if self._validar_valor(alto):
            self._alto = alto       # Variable Privada
        else:
            self._alto = 0
            print(f'[ERROR] Valor erroneo alto: {alto}')
    
    # -----------------------------
    # Métodos SET y GET
    # -----------------------------
    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        if self._validar_valor(nuevo_ancho):
            self._ancho = nuevo_ancho
        else:
            print(f'[ERROR] Valor erroneo nuevo_ancho: {nuevo_ancho}')

    @alto.setter
    def alto(self, nuevo_alto):
        if self._validar_valor(nuevo_alto):
            self._alto = nuevo_alto
        else:
            print(f'[ERROR] Valor erroneo nuevo_alto: {nuevo_alto}')

    def __str__(self):
        return f'[FiguraGeometrica] Ancho: {self._ancho} - Alto: {self.alto}'
    
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
