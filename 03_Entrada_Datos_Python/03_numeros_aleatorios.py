"""
Uso de Números Aleatorios en Python
===================================
Este script muestra cómo generar números aleatorios y simular el lanzamiento de un dado en Python.
"""

# -------------------------------------
# Generación de Números Aleatorios
# -------------------------------------
from random import randint

# -------------------------------------
# Generar un número aleatorio entre 1 y 10
# -------------------------------------
num_aleatorio = randint(1,10)
print(f'Numero aleatorio (entre 1 y 10): {num_aleatorio}')


# -------------------------------------
# Simulación de lanzamiento de un dado
# -------------------------------------
dado = randint(1,6)
print(f'Resultado al lanzar el dado: {dado}')