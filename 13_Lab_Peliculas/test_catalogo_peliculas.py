# ------------------------
# Test Catalogo Peliculas
# ------------------------
from dominio.pelicula import Pelicula
from servicio.catalogo_pelicula import CatalogoPelicula

opcion = None

while opcion != 4:
    try:
        print('Menú: ')
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar Catálogo de Películas')
        print('4. Salir')
        
        opcion = int(input('Seleccione una opción (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPelicula.agregar_pelicula(pelicula)
        elif opcion == 2:
            CatalogoPelicula.listar_peliculas()
        elif opcion == 3:
            CatalogoPelicula.eliminar_peliculas()
    except Exception as e:
        print(f'[ERROR] {e}')
        opcion = None
else:
    print('Saliendo del programa...')