"""
Iterar Listas en Python
=======================
En este script, se muestran ejemplos de cómo iterar a través de listas en Python utilizando un bucle for.
"""

print(f'[ITERACIÓN DE LISTAS]\n')

# ----------------------
# Ejemplo 1: Iterar una lista de nombres
# ----------------------
nombres = ['Jon', 'Arya', 'Sansa']
i = 0 # Contador para la posición

for nombre in nombres:
    print(f'Posicion [{i}]: {nombre}')
    i += 1

print()

# ----------------------
# Ejemplo 2: Iterar una lista mixta
# ----------------------
lista_mixta = [100, False, 'Pepe']
i = 0 # Contador para la posición

for lista in lista_mixta:
    print(f'Posicion [{i}]: {lista}')
    i += 1
