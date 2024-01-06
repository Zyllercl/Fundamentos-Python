
# Set

"""
    Set     -> No mantiene el orden de los elementos
            -> No se puede modificar los elementos ya creados en un set
            -> Se pueden agregar y eliminar elementos
"""

# Definicion de un set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

# Largo de los elementos
print(len(planetas))

# Verificar si existe un elemento dentro de un set
print('Marte' in planetas)

# Agregar un elemento al set
planetas.add('Tierra')
print(planetas)

planetas.add('Tierra') # NO PERMITE ELEMENTOS DUPLICADOS (Solo deja uno)
print(planetas)

# Eliminar un elemento del set
planetas.remove('Tierra')
print(planetas)
# Eliminar un elemento sin arrojar error
planetas.discard('Venus')
print(planetas)

# Eliminar todos los elementos de un set
planetas.clear()
print(planetas)

# Eliminar set
del planetas