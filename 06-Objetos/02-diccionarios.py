
# Iniciar un diccionario vacio
jugador = {}
print(jugador)

# Agregar un nuevo jugador
jugador['nombre'] = 'Mopa'
jugador['puntaje'] = 0
print(jugador)

# Incrementar el puntaje
jugador['puntaje'] = 20
print(jugador)

# Acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))

# Iterar en un diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

# Eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)