"""
Uso de Métodos de Strings en Python
===================================
Este script muestra de cómo utilizar algunos métodos comunes de strings en Python para manipular y obtener información de cadenas de texto.
"""

# ------------------------------------------------------
# Ejemplo de uso de métodos de strings
# ------------------------------------------------------

# Variable original tipo STR
variable_original = 'Hola Mundo'
print(f'Variable Original: {variable_original}')

# ------------------------------------------------------
# Método upper(): convierte a mayúsculas
# ------------------------------------------------------
mayusculas = variable_original.upper()
print(f'Uso de upper(): {mayusculas}')

# ------------------------------------------------------
# Método lower(): convierte a minúsculas
# ------------------------------------------------------
print(f'Uso de lower(): {variable_original.lower()}')

# ------------------------------------------------------
# Método strip(): elimina espacios al inicio y al final
# ------------------------------------------------------
variable_editada = '    Hola Pepe'
print(f'Variable con espacios: {variable_editada}')
print(f'Uso de strip(): {variable_editada.strip()}\n')

# ------------------------------------------------------
# Método len(): obtiene la longitud de la cadena
# ------------------------------------------------------
variable_nueva = 'Hola, Mundo!'
print(f'Variable nueva: {variable_nueva}')
print(f'Largo de la variable nueva: {len(variable_nueva)}')