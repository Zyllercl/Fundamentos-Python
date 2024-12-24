'''     OPERACIONES SET EN PYTHON    '''

from regex import B


print(f'-----   OPERACIONES SET   -----')
# Variables
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f'''\nSets originales:
set a: {set_a}
set b: {set_b}
''')

# Union de sets
union = set_a | set_b   # Los numeros repetidos no se mostrarán por consola
print(f'Union de 2 set: {union}') 

# Interseccion de sets
interseccion = set_a & set_b    # Los valores que coincidan son los que se mostrarán por consola
print(f'\nInterseccion de 2 set: {interseccion}')

# Diferencia de sets
diferencia = set_a - set_b  # Los valores que se repiten en ambos sets se eliminarán del primer conjunto (set_a)
print(f'\nDiferencia de 2 set: {diferencia}')