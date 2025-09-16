"""
Uso de Sets en Python
=====================

Definición:
-----------

Los sets (conjuntos) son colecciones de datos que son:

- MUTABLES, es decir, se pueden modificar.
- NO ORDENADOS, lo que significa que no mantienen un orden específico.
- NO PERMITEN ELEMENTOS DUPLICADOS, es decir, cada elemento debe ser único.

Estos se definen de la siguiente manera:

    1. set_ejemplo = {1, 2, 3, 4, 5}
    2. set_mixto = {1, "Hola", 3.14, True}
    3. set_vacio = set()  # Forma correcta de definir un set vacío
"""

print(f'[SETS EN PYTHON]\n')

# ----------------------
# Ejemplos de Sets en Python
# ----------------------
set_numerico = {1, 2, 3, 4}
set_mixto = {1, "Scar", False, 3.14}
set_numeros = {1, 2, 2, 3, 4, 5}

# Los valores duplicados sólo se tomará el primer elemento encontrado y los demás se descartan.

# ----------------------
# Ejemplo: Los valores duplicados no se almacenan en un set, es decir, se descartan al mostrar por consola
# ----------------------
print(f'{set_numeros}\n')

# ----------------------
# Manejo de Sets en Python
# ----------------------
print(f'[MANEJO DE SETS EN PYTHON]\n')

# ----------------------
# Crear un set
# ----------------------
nuevo_set = {1, 2, 3, 4, 5, 4} # El valor 4 se repetirá pero no se almacenará

print(f'SET Original: {nuevo_set}')

# ----------------------
# Agregar elementos al set
# ----------------------
nuevo_set.add(6)
nuevo_set.add(7)

print(f'SET Modificado: {nuevo_set}\n')

# ----------------------
# Eliminar un elemento del set
# ----------------------
nuevo_set.remove(4)

print(f'Elemento (4) eliminado del set: {nuevo_set}\n')

# ----------------------
# Comprobar si existe un elemento en el set
# ----------------------
print(f'\nExiste el valor de 4 en el set?: {4 in nuevo_set}')
print(f'\nExiste el valor de 1 en el set?: {1 in nuevo_set}')