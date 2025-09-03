"""
Ejemplo de Conversión de Tipos de Datos en Python
=================================================
Este scritp muestra cómo concatenar strings y cómo convertir strings a números en Python.
"""

# -------------------------------------
# Concatenación de Strings
# -------------------------------------
"""
Regla: Si se suman dos strings, se unirán uno al lado del otro sin espacios.
"""
numero_string_1 = '10'
numero_string_2 = '20'

resultado = numero_string_1 + numero_string_2
print(f'Concatenación de Strings: {resultado}\n')

# -------------------------------------
# Conversión de Strings a Números y Suma
# -------------------------------------
numero_entero_1 = int(numero_string_1)
numero_entero_2 = int(numero_string_2)

resultado = numero_entero_1 + numero_entero_2
print(f'Suma de Enteros: {resultado}')