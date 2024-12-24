'''     LISTAS EN PYTHON    '''

print(f'-----   COLECCIONES: LISTAS   -----')
# Ejemplo de listas
numeros = [1, 2, 3, 4, 5]
frutas = ["Manzana", "Pera", "Sandia"]
mixta = [1, "dos", 3.1415, [4,5]]

print(f'{numeros} -> Lista original')

# Obtener el largo de una lista
print(f'Largo de la lista: {len(numeros)}')

# Acceder a los elementos de la lista
print(f'Obtener el valor del indice 4: {numeros[4]}')
print(f'Obtener el último indice de la lista: {numeros[-1]}\n')

'''     CRUD LISTAS    '''
# Agregar un nuevo elemento al final de la lista
numeros.append(6)
print(f'{numeros} -> Lista editada')

# Agregar un nuevo elemento en un índice (posición) en específico
numeros.insert(2, 12)
print(f'Modificacion indice 2 por un: {numeros}')

# Modificar los elementos de una lista
numeros[1] = 11
print(f'Modificación del valor del indice 1 es: {numeros}')

# Eliminar elementos de una lista por su valor
numeros.remove(12)
print(f'Eliminación del elemeneto 12: {numeros}')

# Eliminar un elemento por su indice
print(f'Eliminación del indice 1 con valor: {numeros[1]}')
numeros.pop(1)
print(f'{numeros} -> Lista Modificada')

# Eliminar un elemento usando 'del'
del numeros[0]
print(f'{numeros} -> Eliminación del número 1')

# Generar una sublista (a partir del indice 1 hasta el indice 3, sin incluir este ultimo)
subnumeros = numeros[1:3]
print(f'{subnumeros} -> Sublista generada valores indice 1 y 2')



