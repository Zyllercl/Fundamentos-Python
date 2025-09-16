# --------------------------
# Creación de la Clase
# --------------------------
class Biblioteca:
    # --------------------------
    # Constructor
    # --------------------------
    def __init__(self, nombre):
        # --------------------------
        # Atributos de Instancia
        # --------------------------
        self._nombre = nombre
        self._libros = []

    # --------------------------
    # Métodos GET
    # --------------------------
    @property
    def nombre(self):
        return self._nombre

    @property
    def libros(self):
        return self._libros

    # --------------------------
    # Métodos para Administrar los Libros
    # --------------------------

    # Método para Agregar un Libro
    def agregar_libro(self, libro):
        # Sólo agrega 1 Objeto de tipo Libro
        self._libros.append(libro)

    # Método para Buscar un Libro por Autor
    def buscar_libros_por_autor(self, autor):
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)
    
    # Método para Buscar libros por Genero
    def buscar_libros_por_genero(self, genero):
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)
    
    # Método para Mostrar Información de 1 sólo Libro
    def mostrar_libro(self, libro):
        print(f'Título: {libro.titulo} - Autor: {libro.autor} - Genero: {libro.genero}\n')
    
    # Método para Mostrar Información de Todos los Libros
    def mostrar_todos_los_libros(self):
        print(f'[LIBROS DE LA BIBLIOTECA]\n')
        for libro in self._libros:
            self.mostrar_libro(libro)

    # --------------------------
    # Métodos GET
    # --------------------------
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def libros(self):
        return self._libros
