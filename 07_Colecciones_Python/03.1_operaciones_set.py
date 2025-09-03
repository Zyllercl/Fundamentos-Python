'''     OPERACIONES SET EN PYTHON    '''

"""
Operaciones con Sets en Python
==============================

Definición:
-----------

Las operaciones con Sets permiten realizar diversas manipulaciones y cálculos entre conjuntos de datos. Algunas de las operaciones más comunes incluyen:

- Unión: Combina todos los elementos de dos sets, eliminando duplicados.
- Intersección: Devuelve los elementos que son comunes a ambos sets.
- Diferencia: Devuelve los elementos que están en el primer set pero no en el segundo.

*IMPORTANTE*: Estas operacions son útiles para manejar y comparar conjuntos de datos de manera eficiente.
"""

# ----------------------
# Ejemplo de Operaciones con Sets en Python
# ----------------------
print(f'[OPERACIONES CON SETS EN PYTHON]\n')

# ----------------------
# Definición de dos sets
# ----------------------
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f'''\nSets originales:\n
set a: {set_a}
set b: {set_b}
''')

# ----------------------
# Operaciones con sets
# ----------------------

# Union de sets
union = set_a | set_b   # Los numeros repetidos no se mostrarán por consola
print(f'Union de 2 Set: {union}\n') 

# Intersección de sets
interseccion = set_a & set_b    # Los valores que coincidan son los que se mostrarán por consola
print(f'Interseccion de 2 set: {interseccion}\n')

# Diferencia de sets
diferencia = set_a - set_b  # Los valores que se repiten en ambos sets se eliminarán del primer conjunto (set_a)
print(f'Diferencia de 2 set: {diferencia}\n')