#  Laboratorio Catálogo Películas

---

## Introducción
- Crear una aplicación para la administración de un catálogo de películas. El proyecto estará organizado en una estructura de carpetas y archivos, incluyendo clases específicas para manejar la lógica de dominio y de servicio, así como un archivo de prueba que permitirá interactuar mediante un menú de opciones.

- Esta aplicación permitirá:
    - **1. Agregar películas**
    - **2. Listar las películas**
    - **3. Eliminar el archivo de películas**
    - **4. Salir**

---

## Paso 1: Estructura de carpetas y archivos

📂 13_Lab_Peliculas
- 📂 dominio
    - pelicula.py
- 📂 servicio
    - catalogo_pelicula.py
- test_catalogo_peliculas.py

---

## Paso 2: Crear la clase Pelicula
- Esta clase representa una **película** y contendrá un único **atributo privado** llamado `nombre`. Además, se debe sobreescribir el método `__str__` para mostrar su estado al imprimir el objeto.
- La clase **película** es una **clase de dominio**, ya que representa directamente una película dentro de la lógica del problema. Su objetivo es almacenar y mostrar el nombre de la película cuando sea necesario.

---

## Paso 3: Crear la clase CatalogoPeliculas
- Esta clase actuará como **clase de servicio**, conteniendo los métodos para manipular el archivo y sus películas.

- La clasae debe tener:

    • Una variable estática `ruta_archivo` que contendrá el nombre del archivo (ejemplo: peliculas.txt).
    
    • El método `agregar_pelicula`, que abrirá el archivo en modo append y añadirá una nueva película.
    
    • El método `listar_peliculas`, que mostrará todas las películas guardadas en el archivo.
    
    • El método `eliminar`, que eliminará el archivo utilizando el módulo **os** y su función **remove**.

    •El método `salir`, permitirá cerrar la ejecución del programa.

---

## Paso 4: Crear y Ejecutar TestCatalogoPeliculas

- Crear archivo `test_catalogo_peliculas.py`
- Crear un **menú en consola** con las siguientes opciones:
    - 1 Agregar película
    - 2 Listar películas
    - 3 Eliminar archivo de películas
    - 4 Salir

- El menú se debe implementar con un ciclo `while` donde:
    - Mostrar las opciones de manera repetida
    - Ejecutar la accion elegida por el usuario
    - Terminar la aplicación sólo si el usuario elige la opción 4
    