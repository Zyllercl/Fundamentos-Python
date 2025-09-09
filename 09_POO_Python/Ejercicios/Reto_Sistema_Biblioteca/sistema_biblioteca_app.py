from enum import auto
from biblioteca import Biblioteca

from libro import Libro

# --------------------------
# SISTEMA DE PRUEBAS APP BIBLIOTECA
# --------------------------

biblioteca_santaigo = Biblioteca('BIBLIOTECA DE SANTIAGO')

print(f'[BIENVENIDO A LA {biblioteca_santaigo.nombre}]\n')

# --------------------------
# Creación de objetos de tipo Libro
# --------------------------
libro_1 = Libro('Harry Potter', 'Joanne Rowling', 'Fantasía')
libro_2 = Libro('Ines del Alma Mia', 'Isabel Allende', 'Novela')
libro_3 = Libro('Papelucho', 'Marcela Paz', 'Novela')
libro_4 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Comedia')

# --------------------------
# Agregar libros a la Biblioteca
# --------------------------
biblioteca_santaigo.agregar_libro(libro_1)
biblioteca_santaigo.agregar_libro(libro_2)
biblioteca_santaigo.agregar_libro(libro_3)
biblioteca_santaigo.agregar_libro(libro_4)

# --------------------------
# Buscar libro por Autor
# --------------------------
autor = 'Marcela Paz'
print(f'[LIBROS POR AUTOR]\n')
biblioteca_santaigo.buscar_libros_por_autor(autor)

# --------------------------
# Buscar libro por Genero
# --------------------------
genero = 'Novela'
print(f'[LIBROS POR GENERO]\n')
biblioteca_santaigo.buscar_libros_por_genero(genero)

# --------------------------
# Mostrar todos los libros
# --------------------------
biblioteca_santaigo.mostrar_todos_los_libros()
