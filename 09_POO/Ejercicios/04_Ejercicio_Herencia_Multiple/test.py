from cuadrado import Cuadrado
from rectangulo import Rectangulo
from figura_geometrica import FiguraGeometrica

# -----------------------------
# Probando creación de una FiguraGeometrica
# -----------------------------
# figura = FiguraGeometrica() # Esto genera un ERROR ya que no se puede instanciar una clase de tipo abstracta.

# -----------------------------
# Probando Ejercicio Cuadrado
# -----------------------------
print(f'[CREACION OBJETO CUADRARO]'.center(50,'-'))

# Asignación de los valores 
cuadrado = Cuadrado(lado=5, color='Blanco')
# Cambiando el valor del alto 
cuadrado.alto = 7
# Cambiando el valor del ancho
cuadrado.ancho = 7

# Se muestra los valores de la variable Cuadrado, si los valores ingresados anteriormente estan erroneos, se mantendra el valor original
print(f'{cuadrado}')
# Realiza el calculo del área del cuadrado y lo muestra
print(f'Área de un Cuadrado: {cuadrado.calcular_area()}\n')


# -----------------------------
# Probando Ejercicio Rectangulo
# -----------------------------
print(f'[CREACION OBJETO RECTANGULO]'.center(50,'-'))
rectangulo = Rectangulo(color='Rojo', ancho=3, alto=5)
# Cambiando el valor del ancho
rectangulo.ancho = 100

# Se muestra los valores de la variable Rectangulo, si los valores ingresados anteriormente estan erroneos, se mantendra el valor original
print(rectangulo)
# Realiza el calculo del área del rectangulo y lo muestra
print(f'Área de un Rectangulo: {rectangulo.calcular_area()}\n')
