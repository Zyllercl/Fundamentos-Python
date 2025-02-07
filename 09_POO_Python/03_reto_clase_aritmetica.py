'''
    CLASES ARITMETICAS

    Def: 
        - Crear una clase con los metodos básicos de una calculadora (Suma, Resta, Division, Multiplicacion).
    
    
    [!] Para poder entregar sólo 1 parámetro a un constructor, se deben declarar estas variables con valores predeterminados.
'''

# Definicion de la clase
class Aritmetica:
    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2
    
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
    # Creacion primer objeto
    print('Primer Objeto')
    objeto1 = Aritmetica(2,3)
    objeto1.sumar()
    objeto1.restar()
    # Creacion segundo objeto
    print(f'\nSegundo Objeto')
    objeto2 = Aritmetica(2,5)
    objeto2.multiplicar()
    objeto2.dividir()
    # Creacion tercer objeto (con 1 parametro)
    print(f'\nTercer Objeto (1 parametro)')
    objeto3 = Aritmetica(10)
    objeto3.operando2 = 1
    objeto3.sumar()
    # Creacion cuarto objeto (sin parametros)
    print(f'\nCuarto Objeto (sin parametros)')
    objeto4 = Aritmetica()
    objeto4.operando1 = 2 # Asignacion de valor a la variable operando1
    objeto4.operando2 = 5 # Asignacion de valor a la variable operando2
    objeto4.sumar()
    # Creacion quinto objeto (declaracion de parametros)
    print(f'\nQuinto Objeto (declaracion de parametros)')
    objeto5 = Aritmetica(operando2=4, operando1=3)
    objeto5.sumar()