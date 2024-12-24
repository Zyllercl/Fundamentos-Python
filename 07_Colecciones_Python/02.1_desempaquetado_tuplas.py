'''     DESEMPAQUETADO DE TUPLAS EN PYTHON (UNPACKING)    '''

# El unpacking consiste en extraer los elementos de una tupla y permite asignarlos a diferentes variables

print(f'-----   DESEMPAQUETADO DE TUPLAS (unpacking)   -----')
# Ejemplo de unpacking
tupla = ('P001', 'Polera', 15000)

# Desempaquetado (unpacking)
id, descripcion, precio = tupla

print(f'Tupla completa: {tupla}') # Tupla completa

print(f'ID: {id} - Descripcion: {descripcion} - Precio: {precio}') # Valores independientes ya desempaquetados

