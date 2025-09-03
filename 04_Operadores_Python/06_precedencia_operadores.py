"""
Uso de la precedencia de operadores en Python
=============================================
Este script muestra cómo Python evalúa las expresiones matemáticas según la precedencia de los operadores.
"""
# ---------------------------
# Ejemplo de uso de la precedencia de operadores
# ---------------------------

resultado = 12 / 3 + 2 * 3 - 1

print(f'Resultado: {resultado}')

# Desglose del ejercicio
# 1.- Division: 12 / 3          -> 4
# 2.- Multiplicacion: 2 * 3     -> 6
# 3.- Suma: 4 + 6               -> 10
# 4.- Resta: 10 - 1             -> 9 Valor Final