"""
Desempaquetado de Tuplas en Python (unpacking)
==============================================

Definición:
-----------

- El desempaquetado (unpacking) consiste en extraer los elementos de una tupla y permite asignarlos a diferentes variables.
- Es una forma conveniente de asignar múltiples variables a partir de una tupla.
"""

# ----------------------
# Ejemplo de Desempaquetado de tuplas
# ----------------------
print(f'[DESEMPAQUETADO DE TUPLAS]\n')

# Definición de una tupla
tupla = ('P001', 'Polera', 15000)

# Desempaquetado (unpacking)
id, descripcion, precio = tupla

print(f'Tupla completa: {tupla}') # Tupla completa

print(f'ID: {id} - Descripcion: {descripcion} - Precio: {precio}') # Valores independientes ya desempaquetados

