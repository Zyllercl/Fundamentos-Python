
# Ejercicio de Playlist

# Variables
playlist = { } # Diccionario Vacio
playlist['canciones'] = [] # Lista vacia de canciones

# Funcion principal
def app():
    print('Inicializacion App')    
    # Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        # Variables
        nombre_playlist = input('Ingresa un nombre para la playlist: ')
        if nombre_playlist:
            # Agregando valores al Diccionario
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            # Llamando a la funcion agregar canciones
            agregar_canciones() 
            
def agregar_canciones():
    print('Agregando canciones...')
    agregar_cancion = True

    while agregar_cancion:
        # Variables
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones a la playlist {nombre_playlist} '
        pregunta += '(Para salir presiona "X"): '
        
        cancion = input(pregunta)

        if cancion == 'X':
            # Dejar de agregar canciones
            agregar_cancion = False

            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            # Agregar canciones a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Mostrando resumen de la playlist {nombre_playlist} \n')
    for cancion in playlist['canciones']:
        print(cancion)

app()