from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

# No se puede instanciar una clase Abstracta
# figura = FiguraGeometrica()


# Crear objeto cuadrado
print('Creacion Objeto Cuadrado'.center(50,'-'))
cuadrado = Cuadrado(lado=3, color='Rojo')
cuadrado.alto = 5
cuadrado.ancho = 5
print(f'Area Cuadrado: {cuadrado.calcular_area()}')
print(cuadrado)

print('Creacion Objeto Rectangulo'.center(50,'-'))
rectangulo = Rectangulo(ancho=3, alto=5, color='Verde')
# rectangulo._ancho = 15
print(f'Area Rectangulo: {rectangulo.calcular_area()}')
print(rectangulo)


""""
    MRO - Method Resolution Order
    
    Es importante el orden en que se definen las clases Padres
    
    Orden Original:
    [<class 'Cuadrado.Cuadrado'>, <class 'FiguraGeometrica.FiguraGeometrica'>, <class 'Color.Color'>, <class 'object'>]
    
    Orden Cambiado:
    [<class 'Cuadrado.Cuadrado'>, <class 'Color.Color'>, <class 'FiguraGeometrica.FiguraGeometrica'>, <class 'object'>]
    
    Esto quiere decir que primero resolvera el metodo Cuadrado, posteriormente Color y asi sucesivamente.
    
    print(Cuadrado.mro())
"""

