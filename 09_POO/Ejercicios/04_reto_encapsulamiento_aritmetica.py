"""
RETO: Clases Aritmética con Encapsulamiento (GET y SET)
=======================================================
Este script es similar al "reto_clase_aritmetica.py" con la diferencia de la definición de los Métodos GET y SET para las variables "operando1" y "operando2"
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
        self._operando1 = operando1     # Variable Protegida
        self._operando2 = operando2     # Variable Protegida
    
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
    
    
    # ----------------------------
    # Métodos GET [Decorador @property]
    # ----------------------------
    @property
    def operando1(self):
        return self._operando1

    @property
    def operando2(self):
        return self._operando2
    
    # ----------------------------
    # Métodos SET [Decorador @{atributo}.setter]
    # ----------------------------
    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1
    
    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2


if __name__ == '__main__':
    print('[RETO] Clase Aritmética - Métodos GET y SET\n')
    # ----------------------------
    # Creación Primer Objeto
    # ----------------------------
    print(f'[FUNCION SUMAR]')
    aritmetica = Aritmetica(10,2)
    aritmetica.sumar()

    # ----------------------------
    # Obteniendo valor de la variable "operando2" [Método GET]
    # ----------------------------
    print(f'\n[MÉTODO GET] Valor Operando2: {aritmetica.operando2}\n')

    # ----------------------------
    # Cambiando el valor de las variables [Método SET]
    # ----------------------------
    aritmetica.operando1 = 99
    aritmetica.operando2 = 10

    print('[MODIFICACIÓN VARIABLES (Método SET)]')
    print(f'[MODIFICADO] Operando1: {aritmetica.operando1}')
    print(f'[MODIFICADO] Operando2: {aritmetica.operando2}\n')
    
    aritmetica.sumar()
