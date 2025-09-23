import os

# -------------------------------
# Creación de la clase CatalogoPelicula
# -------------------------------
class CatalogoPelicula:
    # Variables Globales
    RUTA_ARCHIVO = 'peliculas.txt'

    @classmethod # Esto permite acceder a los atributos de clase
    def agregar_pelicula(cls, pelicula):
        with open(cls.RUTA_ARCHIVO, 'a', encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    
    @classmethod
    def listar_peliculas(cls):
        with open(cls.RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
            print(f'\n[CATALOGO DE PELÍCULAS]')
            # Leer todas las líneas del archivo y mostrarlas
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        # Eliminación del archivo
        os.remove(cls.RUTA_ARCHIVO)
        print(f'[DELETE] Se ha eliminado el archivo: {cls.RUTA_ARCHIVO}')