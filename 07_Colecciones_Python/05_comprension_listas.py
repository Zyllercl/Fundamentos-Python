"""
Uso de la Comprensión de Listas (List Comprehension) en Python
==============================================================
Este script demuestra cómo utilizar la comprensión de listas para crear nuevas listas de manera concisa y eficiente.
"""

print(f'[LIST COMPREHENSION]\n')

# ------------------------------
# Ejemplo 1: Lista sólo los numeros pares de una lista
# ------------------------------
numeros = [1, 2, 3, 4, 5, 6]

pares = [x for x in numeros if x % 2 == 0]

print(f'Numeros pares: {pares}')

# ------------------------------
# Ejemplo 2: Lista el valor al cuadrado de cada numero
# ------------------------------
cuadrado = [x**2 for x in numeros]

print(f'Numeros: {cuadrado}\n')

# ------------------------------
# Ejemplo 3: Listar un saludo a varios nombres de una lista
# ------------------------------
nombres = ['Pepe', 'Clara', 'Jon']

saludar = [f'Hola {nombre}' for nombre in nombres]

print(saludar)