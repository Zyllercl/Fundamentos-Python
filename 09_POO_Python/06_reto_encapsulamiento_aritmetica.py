'''
    CLASES ARITMETICAS

    Modificación de los atributos y creacicón de GET y SET para cada atributo.
'''

# Definicion de la clase
class Aritmetica:
    def __init__(self, operando1=None, operando2=None):
        # Atributos 
        self._operando1 = operando1
        self._operando2 = operando2
    
    # Funciones Aritmeticas
    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'La suma de {self._operando1} y {self._operando2} es: {resultado}')

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'La resta de {self._operando1} y {self._operando2} es: {resultado}')
    
    def multiplicar(self):
        resultado = self._operando1 * self._operando2
        print(f'La multiplicacion de {self._operando1} y {self._operando2} es: {resultado}')

    def dividir(self):
        resultado = self._operando1 / self._operando2
        print(f'La division de {self._operando1} y {self._operando2} es: {resultado}')

    # Decorador Property (GET)
    @property
    def operando1(self):
        return self._operando1

    @property
    def operando2(self):
        return self._operando2
    
    # Decorador Setter (SET)
    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1
    
    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2

if __name__ == '__main__':
    # Creacion primer objeto
    aritmetica = Aritmetica(10,2)
    aritmetica.sumar()

    # Obteniendo el operando2 (GET)
    print(f'[ORIGINAL] Operando 2: {aritmetica.operando2}')

    # Cambiar el operando 2 (SET)
    aritmetica.operando2 = 10
    print(f'[MODIFICADO] Operando2: {aritmetica.operando2}')
    aritmetica.sumar()