import os

class CatalogoPeliculas:
    # Variables Globales
    ruta_archivo = 'peliculas.txt'
    
    @classmethod # Permite acceder a los atributos de clases (variables globales)
    def agregar_pelicula(cls, pelicula):
        # Apertura del archivo
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.get_nombre()}\n')
            # Una vez terminada la escritura se cierra el archivo
    
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catalogo de Peliculas'.center(50,'-'))
            print(archivo.read()) # Lectura del archivo
    
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'[!] Archivo eliminado: {cls.ruta_archivo}')