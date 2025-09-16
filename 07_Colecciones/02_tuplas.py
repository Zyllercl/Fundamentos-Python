"""
Uso de Tuplas en Python
=======================

Definición:
-----------

- Las tuplas son colecciones de datos que son INMUTABLES, es decir, no se pueden modificar.
- Se definen utilizando paréntesis `()` o simplemente separando los elementos con comas.
- Pueden contener elementos de diferentes tipos de datos (números, cadenas, listas, etc.).
- Son útiles para almacenar datos que no deben cambiar a lo largo del tiempo.

*IMPORTANTE*:
- Los objetos de tipo Tupla no soporta la asignación de elementos, es decir, no se pueden cambiar, agregar o eliminar elementos después de su creación.

Por ejemplo:

    tupla_numeros = (1, 2, 3, 4, 5)
    tupla_numeros[0] = 10   # Error al cambiar un elemento por otro
    tupla_numeros.append(6) # Error al agregar un elemento a la tupla
"""

print(f'[TUPLAS EN PYTHON]\n')

# ----------------------
# Ejemplo de Tuplas en Python
# ----------------------
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mixta = ("sandia", 10, 3.1415, [1, 2, 3])
tupla_sin_parentesis = "Pepe", "Murphy"
tupla_un_elemento = 10, # La coma es obligatoria

# ----------------------
# Operaciones básicas con tuplas
# ----------------------

# Recorrer una tupla con un bucle for
print(f'Recorriendo la tupla con un bucle for:')
for elemento in tupla_numeros:
    print(elemento, end=' ')

# Crear una tupla de tipo coordenada (x, y)
coordenadas = (3, 7)

# Obtener cada elemento de la tupla "coordenadas"
print(f'\n\nCoordenada X: {coordenadas[0]}')
print(f'Coordenada Y: {coordenadas[1]}')

# Tupla de un sólo elemento
print(f'\nTupla de un elemento: {tupla_un_elemento}')

# ----------------------
# Desempaquetado de tuplas (unpacking)
# ----------------------
print(f'\nDESEMPAQUETADO DE TUPLAS (Unpacking)\n')
tuplas_anidadas = (1, (2, 3), (4, 5))
print(f'Tupla anidada: {tuplas_anidadas}')
print(f'Segundo elemento tupla anidada: {tuplas_anidadas[1]}')