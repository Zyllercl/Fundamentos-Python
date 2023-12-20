
# Listas o Arreglos en Python

# Variables
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

print(f'Primera posicion: {lenguajes[0]}')

# Ordenar los elementos alfabeticamente
lenguajes.sort()
print(f'Lista ordenada alfabeticamente: {lenguajes}')

# Acceder a un elemento dentro de un texto
mensaje = f'Estoy aprendiendo {lenguajes[3]}'
print(mensaje)

# Eliminar un elemento y reemplazar
lenguajes[2] = 'PHP'
print(f'Modificando Kotlin por PHP: {lenguajes}')

# Agregar elementos a un arreglo (list)
nuevo_lenguaje = 'Bash'
lenguajes.append(nuevo_lenguaje)
print(f'Se agrego {nuevo_lenguaje} al arreglo: {lenguajes}')

# Eliminar un elemento de un arreglo (list)
del lenguajes[4]
print(f'Se elimino "Bash" del arreglo: {lenguajes}')

# Eliminar el ultimo elemento de un arreglo (list)
lenguajes.pop()
print(f'Se elimino el ultimo elemento del arreglo: {lenguajes}')

# Eliminar un elemento especifico de un arreglo (list)
lenguajes.pop(2)
print(f'Se elimino PHP del arreglo: {lenguajes}')

# Eliminar un elemento por nombre de un arreglo (list)
lenguajes.remove('Java')
print(f'Se elimino Java del arreglo: {lenguajes}')