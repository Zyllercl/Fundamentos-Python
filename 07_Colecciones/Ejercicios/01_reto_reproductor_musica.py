"""
RETO: Lista de reproducción
===========================

Definición:
-----------

Crear un programa para administrar una lista de canciones. Debes solicitar al usuario cuantas canciones desea agregar a la lista y posteriormente ir solicitando cada canción que desea agregar a la lista. Se debe mostrar la lista de canciones en orden alfabético.
"""

print(f'[RETO] Lista de reproducción\n')

# --------------------
# Variables
# --------------------
lista_reproduccion = [] # Lista vacia
cantidad_canciones = int(input('¿Cuantas canciones quieres agregar a la playlist?: '))

# --------------------
# Iteracion de cada elemento de la lista para agregar un nuevo elemento
# --------------------
for indice in range(cantidad_canciones):
    # Solicitar nombre de la canción al usuario
    cancion = input(f'Escribe la cancion {indice +1}: ')
    # Agregar canción a la lista
    lista_reproduccion.append(cancion)

# --------------------
# Ordenar la lista de canciones (Ascendente)
# --------------------
lista_reproduccion.sort()

# --------------------
# Ordenar la lista de canciones (Descendente)
# --------------------
# lista_reproduccion.sort(reverse=True) 

print('\n[+] Tu lista de reproducción es:')

for cancion in lista_reproduccion:
    print(f'- {cancion}')