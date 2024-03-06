from abc import ABC, abstractmethod

# ABS = Abstract Base Class

# Si se define un metodo abstracto en una clase, toda la clase se convierte en una clase abstracta

# Clase Padre
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho): 
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
            
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')
    
    # Metodo Abstracto Area
    @abstractmethod
    def calcular_area(self):
        pass
    
    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'
    
    def _validar_valor(self, valor):
        return True if  0 < valor < 10 else False

    """
    Decoradores
            @property -> Permite obtener el valor de una variable y este se podrá obtener a traves de un metodo como un atributo.
            @setter   -> Decorador setter permite cambiar el valor de una variable.
    """
    # Getters y Setters
    @property
    def get_ancho(self):
        return self._ancho

    @get_ancho.setter
    def set_ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')
            
    @property
    def get_alto(self):
        return self._alto
    
    @get_alto.setter
    def set_alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')
