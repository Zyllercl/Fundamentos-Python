"""
RETO: Clases Aritmética
=======================

Definición:
-----------

Crear una Clase con los Métodos Básicos de una Calculadora (Suma, Resta, División, Multiplicación).
"""
# ----------------------------
# Creación de la Clase
# ----------------------------
class Aritmetica:
    # ----------------------------
    # Constructor
    # ----------------------------
    def __init__(self, operando1=None, operando2=None):
        # Variables de Instancia
        self.operando1 = operando1
        self.operando2 = operando2
    
    # ----------------------------
    # Métodos de la Clase (funciones)
    # ----------------------------
    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'La suma de {self.operando1} y {self.operando2} es: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'La resta de {self.operando1} y {self.operando2} es: {resultado}')
    
    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'La multiplicacion de {self.operando1} y {self.operando2} es: {resultado}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'La division de {self.operando1} y {self.operando2} es: {resultado}')


if __name__ == '__main__':
    print('[RETO] Clases Aritmética\n')
    # ----------------------------
    # Creación Primer Objeto
    # ----------------------------
    print('[PRIMER OBJETO]')
    objeto1 = Aritmetica(2,3)
    objeto1.sumar()
    objeto1.restar()

    # ----------------------------
    # Creación Segundo Objeto
    # ----------------------------
    print(f'\n[SEGUNDO OBJETO]')
    objeto2 = Aritmetica(2,5)
    objeto2.multiplicar()
    objeto2.dividir()

    # ----------------------------
    # Creación Tercer Objeto [con 1 parámetro]
    # ----------------------------
    print(f'\n[TERCER OBJETO (con 1 parámetro)]')
    objeto3 = Aritmetica(10)    # Se declara el primer operando
    objeto3.operando2 = 1       # Declaración del segundo operando
    objeto3.sumar()

    # ----------------------------
    # Creación Cuarto Objeto [sin parámetros]
    # ----------------------------
    print(f'\n[CUARTO OBJETO (sin parámetros)]')
    objeto4 = Aritmetica()
    objeto4.operando1 = 2       # Asignacion de valor a la variable operando1
    objeto4.operando2 = 5       # Asignacion de valor a la variable operando2
    objeto4.sumar()

    # ----------------------------
    # Creación Quinto Objeto [declaración de parámetros]
    # ----------------------------
    print(f'\n[QUINTO OBJETO (declaración de parámetros)]')
    objeto5 = Aritmetica(operando2=4, operando1=3)      # Declaración de parámetros 
    objeto5.sumar()