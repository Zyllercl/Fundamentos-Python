# String en Python Avanzado

"""
#   Funcion Help    #
import math
# Mostrar ayuda de un metodo completo
help(str)

# Mostrar ayuda de un metodo en especifico de help
help(str.capitalize)

# Mostrar ayuda de math
help(math)

# Mostrar ayuda de un metodo especifico de math
help(math.nan)
"""

from ej_docstring import docstring

# Revisar archivo ej_docstring.py
# help(docstring) 

# Mostrar solo el docstring de la Clase (No incluye los metodos)
print(docstring.__doc__)

# Mostrar documentacion del metodo __init__
print(docstring.__init__.__doc__)

# Mostrar documentacion de un metodo especifico
print(docstring.mi_metodo.__doc__)

# Comprobar que un metodo es un objeto
print(docstring.mi_metodo) # Retornara la direccion de memoria del objeto

# Saber que tipo de objeto es en Python
print(type(docstring.mi_metodo))