
# Iniciar un diccionario vacio
jugador = {}
print(jugador)

# Agregar un nuevo jugador
jugador['nombre'] = 'Mopa'
jugador['puntaje'] = 0

# Incrementar el puntaje
jugador['puntaje'] = 20

# Acceder a un valor
# print(jugador.get('consola', 'No existe ese valor'))

# Iterar en un diccionario
for llave, valor in jugador.items():
    print(llave, valor)

# Comprobar si existe algun elemento
print('nombre' in jugador)

# Eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)

# Eliminar un elemento de un diccionario
# jugador.pop('nombre')

# Eliminar todos los elementos de un diccionario
# jugador.clear()

# Eliminar un diccionario
# del jugador