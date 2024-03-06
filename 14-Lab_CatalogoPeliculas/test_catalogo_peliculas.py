from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

# Creacion del Menu
opcion = None

while opcion != 4:
    try:
        print('\n### MENU ###')
        print('1. Agregar Peliculas')
        print('2. Listar Peliculas')
        print('3. Eliminar catalogo de peliculas')
        print('4. Salir')
        opcion = int(input('Selecciona una opcion (1-4): '))
        
        if opcion == 1:
            nombre_pelicula = input('Ingresa el nombre de una pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula) # Agrega una pelicula al archivo peliculas.txt
        elif opcion == 2:
            cp.listar_peliculas() # Imprime el catalogo de peliculas del archivo peliculas.txt
        elif opcion == 3:
            cp.eliminar_peliculas() # Elimina todas las peliculas dentro del archivo peliculas.txt
    except ValueError as e:
        print('[ValueError] Ingrese un numero por favor!!!')
    except Exception as e:
        print(f'Ocurrio un error... {e}')
else:
    print('Saliendo del programa...')