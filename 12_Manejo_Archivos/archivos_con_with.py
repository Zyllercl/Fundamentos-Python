"""
Manejo de Archivos con 'with' en Python
=======================================
El uso de la declaración 'with' en Python para manejar archivos es una práctica recomendada, ya que garantiza que los archivos se cierren correctamente después de su uso, incluso si ocurre un error durante las operaciones de archivo. Esto ayuda a prevenir fugas de recursos y otros problemas relacionados con el manejo de archivos, esto se denomina "context manager".
"""

# --------------------------------
# Ejemplo Base de Manejo de Archivos con 'with'
# --------------------------------
# with open('test.txt', 'r', encoding='utf-8') as archivo:
    # Lectura del contenido del archivo
    # print(archivo.read())

# --------------------------------
# Manejo de Archivos con Clase Personalizada y 'with'
# --------------------------------
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('test.txt') as archivo:
    # Lectura del contenido del archivo
    print(archivo.read())