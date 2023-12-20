
# Objetos

"""
    Que son los objetos -> Un objeto es similar a una array, te permite agrupar contenido de diferentes tipos de datos.
                        -> Para acceder a un elemento de un array por medio de un incide, en un objeto se accede mediante una llave (Key)
                        -> Los objetos en Python son denominados Diccionarios (Dictionary)
"""

# Creacion de un diccionario (Objeto)
cancion = {
     # Llave    # Valor
    'artista': 'Metallica',
    'cancion': 'Nothing else mathers',
    'lanzamiento': 1994,
    'likes': 1000
}

# Acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['cancion'])

# Agregar un nuevo valor al diccionario
cancion['playlist'] = 'Heavy Metal'
print(cancion)

# Reemplazar un valor existente
cancion['cancion'] = 'Ones'
print(cancion)

# Eliminar un valor existente
del cancion['likes']
print(cancion)