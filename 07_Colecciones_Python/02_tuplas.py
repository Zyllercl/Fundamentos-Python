'''     TUPLAS EN PYTHON    '''

print(f'-----   COLECCIONES: TUPLAS   -----')
# Ejemplo de tuplas
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mixta = ("sandia", 10, 3.1415, [1, 2, 3])
tupla_sin_parentesis = "Bellamy", "Clarke"
tupla_un_elemento = 10, # La coma es obligatoria


'''
    Los objetos de tipo Tupla no soporta la asignacion de elementos

    tupla_numeros[0] = 10   # Error al cambiar un elemento por otro
    tupla_numeros.append(6) # Error al agregar un elemento a la tupla
'''

for elemento in tupla_numeros:
    print(elemento, end=' ')

# Crear una tupla de tipo coordenada (x, y)
coordenadas = (3, 7)

# Obtener cada elemento
print(f'\n\nCoordenada X: {coordenadas[0]}')
print(f'Coordenada Y: {coordenadas[1]}')

# Tupla de un sólo elemento
print(f'\nTupla de un elemento: {tupla_un_elemento}')

# Tupla anidada
tuplas_anidadas = (1, (2, 3), (4, 5))
print(f'\nTupla anidada: {tuplas_anidadas}')
print(f'Segundo elemento tupla anidada: {tuplas_anidadas[1]}')