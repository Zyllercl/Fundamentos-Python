"""
Uso de Operadores de Asignación en Python
=========================================
Este script muestra cómo utilizar los operadores de asignación en Python.
"""

# ----------------------------------
# Ejemplo de uso de Operadores de Asignación
# ----------------------------------
print(f'-----   Operador Asignación   -----')
numero = 1000
texto = 'Hola Mundo'
print(f'Variable Númerica: {numero}')
print(f'Variable Texto: {texto}\n')

# ----------------------------------
# Ejemplo operador Asignación Múltiple
# ----------------------------------
print(f'-----   Operador Asignación Múltiple   -----')
a, b, c = 'Hola', 100, 35.67
print(f'Variables Múltiples:\n a: {a}\n b: {b}\n c: {c}\n')

# ----------------------------------
# Ejemplo operador Asignación Encadenada
# ----------------------------------
print(f'-----   Operador Asignación Encadenada   -----')
contador1 = contador2 = 1
print(f'Variables Encadenadas:\n Contador1: {contador1}\n Contador2: {contador2}\n')

# ----------------------------------
# Ejemplo de Intercambio de Valores de una variable (Sin utilizar Variables Temporales)
# ----------------------------------
print(f'-----   Intercambio de Valores   -----')
x, y = 1, 5
print(f'Valores Originales\n X: {x}\n Y: {y}')
x,y = y, x
print(f'Variables Invertidas\n X: {x}\n Y: {y}\n')

# ----------------------------------
# Ejemplo de ingresar múltiples valores de entrada
# ----------------------------------
print(f'-----   Ingreso Multiples Valores   -----')
nombre, apellido = input('Ingrese su nombre y apellido (separado por una coma): ').split(',')
print(f'Nombre: {nombre.strip()} , Apellido: {apellido.strip()}')