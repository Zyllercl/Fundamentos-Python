"""
Uso de Operadores Lógicos en Python
===================================
Este script demuestra el uso de operadores lógicos en Python, que son fundamentales para la toma de decisiones en programación.
"""

# Operador Lógico AND
print(f'-----   Operador Lógico AND   -----')
condicion1 = False
condicion2 = True
resultado = (condicion1 and condicion2)
print(f'La condición {condicion1} and {condicion2}: {resultado}\n')

# Operador Lógico OR
print(f'-----   Operador Lógico OR   -----')
condicion1 = False
condicion2 = True
resultado = (condicion1 or condicion2)
print(f'La condición {condicion1} or {condicion2}: {resultado}\n')

# Operador Lógico NOT
print(f'-----   Operador Lógico NOT   -----')
condicion = False
resultado = not condicion
print(f'La condicion NOT {condicion} es: {resultado}\n')

nombre = ''
es_string_vacio = not nombre
print(f'La variable NO tiene ningún valor?: {es_string_vacio}')

variable = None
es_variable_sin_valor = not variable
print(f'La variable NO tienen ningún valor asignado?: {es_variable_sin_valor}')