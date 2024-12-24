'''     SETS EN PYTHON    '''

print(f'-----   COLECCIONES: SET   -----')
# Ejemplo de sets
set_numerico = {1, 2, 3, 4}
set_mixto = {1, "Scar", False, 3.14}
set_numeros = {1, 2, 2, 3, 4, 5}

# Los valores duplicados sólo se tomará el primer elemento encontrado y los demás se descartan.
print(set_numeros)

'''     MANEJO DE SETS    '''
print(f'\n-----   MANEJO DE SETS   -----')

# Crear un conjunto set
nuevo_set = {1, 2, 3, 4, 5, 4}

print(f'Set original: {nuevo_set}')

# Agregar elementos al set
nuevo_set.add(6)
nuevo_set.add(7)

print(f'Set modificado: {nuevo_set}')

# NO SE PUEDE AGREGAR UN VALOR DUPLICADO: nuevo_set.add(3)

# Eliminar un elemento del set
nuevo_set.remove(4)

print(f'Elemento eliminado del set: {nuevo_set}')

# Comprobar si existe un elemento en el set
print(f'\nExiste el valor de 4 en el set?: {4 in nuevo_set}')
print(f'\nExiste el valor de 1 en el set?: {1 in nuevo_set}')