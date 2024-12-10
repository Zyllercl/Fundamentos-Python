'''
    VALOR DENTRO DE RANGO

    Def:
        - Crear un programa que solicite al usuario ingresar un valor entre 0 y 5 e indicar si el valor esta dentro del rango imprimir True, de lo contrario False. Para ello se deben definir 2 constantes:
            - VALOR_MINIMO = 0
            - VALOR_MAXIMO = 5
'''

print(f'-----   VALOR DENTRO DE RANGO   -----')
# Variables
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

numero = int(input('Ingrese un número entero: '))

resultado = (VALOR_MINIMO <= numero <= VALOR_MAXIMO)

print(f'El numero {numero} se encuentra entre {VALOR_MINIMO} y {VALOR_MAXIMO}?: {resultado}')