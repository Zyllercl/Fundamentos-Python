"""
Uso de Operadores de Asignación Compuestos en Python
====================================================
Este script muestra cómo utilizar los operadores de asignación compuestos en Python.
"""

# ----------------------------------
# Ejemplo de uso de Operadores de Asignación Compuestos
# ----------------------------------

# ------------------------------
# Variables Globales
# ------------------------------
a, b = 7, 2
print(f'Variables Iniciales:\n a: {a}\n b: {b}\n')

# ------------------------------
# Ejemplo de Operador Compuesto de Suma ( += )
# ------------------------------
print(f'-----   Operador Compuesto Suma   -----')
a += b
print(f'Operador compuesto a += b es: {a}\n')

# ------------------------------
# Ejemplo de Operador Compuesto de Resta ( -= )
# ------------------------------
print(f'-----   Operador Compuesto Resta   -----')
a -= b
print(f'Operador compuesto a -= b es: {a}\n')

# ------------------------------
# Ejemplo de Operador Compuesto de Multiplicación ( *= )
# ------------------------------
print(f'-----   Operador Compuesto Multiplicación   -----')
a = 9
a *= b
print(f'Operador compuesto a *= b es: {a}\n')

# ------------------------------
# Ejemplo de Operador Compuesto de División ( /= )
# ------------------------------
print(f'-----   Operador Compuesto División   -----')
a = 7
a /= b
print(f'Operador compuesto a /= b es: {a:.2f}\n')