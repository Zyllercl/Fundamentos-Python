"""
Uso de Concatenación de Strings en Python
=========================================
Este script muestra cómo concatenar cadenas de texto en Python.
"""

# -------------------------------------
# Ejemplo de uso de concatenación
# -------------------------------------

# Operador +
string_1 = "Hola"
string_2 = "Mundo"
concatenacion = string_1 + ' ' + string_2
print('Uso de Operador +:', concatenacion)

# Operador join()
concatenacion = ''.join([string_1, ' ', string_2])
print('Uso de Operador JOIN:', concatenacion)