"""
Manejo de Archivos en Python
============================
Este script muestra cómo manejar archivos en Python, se enfocará en la creación de un archivo txt, la escritura de datos en él, la lectura de los datos y el manejo de excepciones.

Tipos de Modos de Manejo de Archivos:
-------------------------------------
- 'r' : Modo lectura (por defecto). El archivo debe existir.
- 'w' : Modo escritura. Crea un archivo nuevo o sobrescribe uno existente
- 'a' : Modo anexar. Añade datos al final del archivo sin borrar el contenido existente.
- 'x' : Modo creación. Crea un archivo nuevo, falla si el archivo ya existe.

- 'b' : Modo binario. Se usa junto con otros modos para archivos binarios (ej. 'rb', 'wb').
- 't' : Modo texto (por defecto). Se usa junto con otros modos para archivos de texto (ej. 'rt', 'wt').
"""

# --------------------------------
# Manejo de Archivos - Escritura
# --------------------------------
try:
    # Crear/Abrir un archivo en modo escritura ('w')
    archivo = open('test.txt', 'w', encoding='utf-8')

    # Escribir datos en el archivo
    archivo.write('Hola, Bienvenido.\n')
    archivo.write('Este es un archivo de prueba para manejo de archivos en Python.\n')
    archivo.write('Esta es una tercera linea de prueba.\n')
except Exception as e:
    print(f'[ERROR] {e}')
finally:
    # Cerrar archivo si fue abierto
    archivo.close()
    print('Archivo cerrado después de la escritura.')

    # Si se desea escribir en el archivo después de cerrarlo, se generará un ERROR.
    # archivo.write('Esto generará un error porque el archivo está cerrado.\n')