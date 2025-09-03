"""
Combinación de Listas y Tuplas en Python
========================================

Definición:
-----------

Definir una lista que almacene tuplas de productos (recordar, las tuplas son INMUTABLES)
"""

# ----------------------
# Ejemplo de combinación de listas y tuplas
# ----------------------
print(f'[COMBINACIÓN DE LISTAS Y TUPLAS]\n')

# ----------------------
# Lista de tuplas (productos)
# ----------------------
lista_productos = [
    ('P001', 'Teclado', 35000), # Tupla 1
    ('P002', 'Mouse', 78000),   # Tupla 2
    ('P003', 'Monitor', 180000) # Tupla 3
]

# ----------------------
# Recorrer la lista de tuplas e imprimir cada producto
# ----------------------
precio_total = 0    # Acumulador del precio total
posicion = 1        # Contador de posición

for producto in lista_productos:
    # Mostrar la tupla completa ha desempaquetar
    print(f'Tupla {posicion}: {producto}')

    # Desempaquetado de la tupla en variables individuales
    id, descripcion, precio = producto
    
    # Imprimir el producto actual
    print(f'Producto {posicion}: id = {id} ; descripcion = {descripcion} ; precio = {precio}\n')

    # Acumular el precio total
    precio_total += precio # O acceder al indice (posicion) de la tupla, es decir, producto[2]
    posicion += 1

print(f'El total es de: ${precio_total}')