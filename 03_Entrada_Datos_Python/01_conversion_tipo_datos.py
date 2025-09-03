"""
Uso de Conversión de Tipos de Datos en Python
=============================================
Este script muestra cómo realizar conversiones entre distintos tipos de datos en Python.
"""

# -------------------------------------
# Conversión de cadena a entero
# -------------------------------------
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Conversión de String a Entero: {numero_entero}')

# -------------------------------------
# Conversión de cadena a flotante
# -------------------------------------
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Conversión de String a Flotante: {numero_flotante}')

# -------------------------------------
# Conversión de número a cadena
# -------------------------------------
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Conversión de Número a String: {numero_cadena}')

# -------------------------------------
# Conversión a booleano
# -------------------------------------
"""
Reglas de conversión a booleano:
- 0, None o cadena vacía -> False
- Cualquier otro valor distinto de 0, None o cadena vacía -> True
"""

# Ejemplos con enteros
numero_entero = 0
print(f'Conversión de Número 0 a Booleano: {bool(numero_entero)}') # False

numero_entero = 1
print(f'Conversión de Número 5 a Booleano: {bool(numero_entero)}') # True

# Ejemplos con strings
cadena = ''
print(f'Conversión de String vacío a Booleano: {bool(cadena)}') # False

cadena = 'String con Valor'
print(f'Conversión de String NO vacío a Booleano: {bool(cadena)}') # True

variable = None
print(f'Conversión de None a Booleano: {bool(variable)}') # False
