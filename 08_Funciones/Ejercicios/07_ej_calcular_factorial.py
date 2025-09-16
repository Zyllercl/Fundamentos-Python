"""
Ejemplo: Calcular el Factorial de un número
===========================================

Definición:
-----------

Crear una función recursiva que permita calcular el Factorial de un número.

Considerar lo siguiente:

    1. Factorial de 0! = 1
    2. Factorial de 1! = 1
"""

print(f'[EJEMPLO] Calcular el Factorial de un número\n')

# -----------------------
# Definición Función Recursiva
# -----------------------

def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        # Aplicando la recursividad
        factorial_parcial = numero * calcular_factorial(numero - 1)

        return factorial_parcial

numero = int(input('Ingrese un número: '))

resultado = calcular_factorial(numero)

print(f'\nEl factorial de {numero} es: {resultado}')
