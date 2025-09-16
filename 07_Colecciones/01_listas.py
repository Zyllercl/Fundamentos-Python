"""
Uso de Listas en Python
=======================

Definición:
-----------

- Las listas son colecciones de datos que son MUTABLES, es decir, se pueden modificar.
- Se definen utilizando corchetes `[]`.
- Pueden contener elementos de diferentes tipos de datos (números, cadenas, listas, etc.).
- Son útiles para almacenar colecciones de datos que pueden cambiar a lo largo del tiempo.
"""

print(f'[LISTAS EN PYTHON]\n')

# -----------------------
# Ejemplos de Listas en Python
# -----------------------
lista_numeros = [1, 2, 3, 4, 5]
lista_frutas = ["Manzana", "Pera", "Sandia"]
lista_mixta = [1, "dos", 3.1415, [4,5]]

print(f'Lista de números: {lista_numeros}\n')

# -----------------------
# Operaciones básicas con listas
# -----------------------

# Obtener el largo de una lista
print(f'Largo de la lista: {len(lista_numeros)}')

# Acceder a los elementos de la lista
print(f'Obtener el valor del indice[4]: {lista_numeros[4]}') # Imprimira el valor 5
print(f'Obtener el valor del último indice de la lista: {lista_numeros[-1]}\n') # Imprimira el valor 5

# -----------------------
# CRUD: Crear, Leer, Actualizar, Borrar elementos en una lista
# -----------------------

# Creación de una nueva lista a partir de la original
lista_modificada = lista_numeros
# Agregar un nuevo elemento al final de la lista con la función 'append()'
lista_modificada.append(6)
print(f'Lista modificada: {lista_modificada}\n')

# Insertar un nuevo elemento en un indice específico
lista_modificada.insert(2, 12) 
print(f'Actualiza el valor de la posición con índice[2]: {lista_modificada}\n')

# Actualizar/modificar un valor en un indice específico
lista_modificada[1] = 11 # Cambia el valor en el indice 1
print(f'Modificación del valor del índice[1]: {lista_modificada}\n')

# Eliminar elementos de una lista por su valor
lista_modificada.remove(12)
print(f'Eliminación del elemeneto 12: {lista_modificada}\n')

# Eliminar un elemento por su índice usando la función 'pop()'
print(f'Eliminación del indice[1]: {lista_modificada[1]}\n')
lista_modificada.pop(1)
print(f'Nueva lista modificada: {lista_modificada}\n')

# Eliminar un elemento usando 'del'
del lista_modificada[0] # Elimina el primer elemento de la lista
print(f'Eliminación del primer elemento de la lista: {lista_modificada}\n')

# -----------------------
# Generar una sublista (a partir del indice 1 hasta el indice 3, sin incluir este ultimo)
# -----------------------
sublista = lista_modificada[1:3]
print(f'Sublista de la lista original (índices 1 a 3): {sublista}\n') # No incluye el índice 3, es decir, el valor 6



