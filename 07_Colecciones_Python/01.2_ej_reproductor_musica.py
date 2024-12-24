'''
    LISTA DE REPRODUCCION

    Def: 
        - Crear un programa para administrar una lista de canciones. Debes solicitar al usuario cuantas canciones desea agregar a la lista y posteriormente ir solicitando cada canción que desea agregar a la lista. Se debe mostrar la lista de canciones en orden alfabético.
'''

print(f'-----   REPRODUCTOR DE CANCIONES   -----')
# Variables
lista_reproduccion = []
cantidad_canciones = int(input('¿Cuantas canciones quieres agregar a la playlist?: '))

# Iteracion de cada elemento de la lista para agregar un nuevo elemento
for indice in range(cantidad_canciones):
    cancion = input(f'Escribe la cancion {indice +1}: ')
    lista_reproduccion.append(cancion)

# Ordenar lista ASC
lista_reproduccion.sort()

# Ordenar lista DESC: lista_reproduccion.sort(reverse=True) 

print('Listado de canciones orden alfabético')
for cancion in lista_reproduccion:
    print(f'- {cancion}')