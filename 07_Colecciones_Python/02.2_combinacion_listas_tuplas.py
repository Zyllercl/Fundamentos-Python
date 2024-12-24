'''
    COMBINACION DE LISTAS Y TUPLAS

    Def:
        - Definir una lista que almacene tuplas de productos (recordar, las tuplas son INMUTABLES)
'''

print(f'-----   COMBINACION DE LISTAS Y TUPLAS   -----')
# Variables
productos = [
    ('P001', 'Teclado', 35000), # Tupla 1
    ('P002', 'Mouse', 78000), # Tupla 2
    ('P003', 'Monitor', 180000) # Tupla e
]

# Imprimir la data de cada producto (tupla) y calcular el precio total
precio_total = 0
posicion = 1

for producto in productos:
    # Unpacking
    id, descripcion, precio = producto
    print(f'Producto {posicion}: id = {id}, descripcion = {descripcion}, precio = {precio}')
    precio_total += precio # O acceder al indice (posicion) de la tupla, es decir, producto[2]
    posicion += 1

print(f'El total es de: ${precio_total}')