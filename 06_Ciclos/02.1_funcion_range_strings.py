"""
Uso de función RANGE en Python - Strings
========================================

Definición:
-----------

La función 'range' puede ser utilizada para iterar un número específico de veces, lo que es útil cuando se desea repetir una acción con cadenas de texto (strings).
"""

print(f'[FUNCION RANGE - STRINGS]\n')

# ---------------------
# Ejemplo: Repetir un mensaje un número específico de veces
# ---------------------
mensaje = input('Escrime un mensaje a repetir: ')
repeticiones = int(input('Ingresa el número de repeticiones: '))

# ---------------------
# Iteración para un rango específico de repeticiones
# ---------------------
for i in range(repeticiones):
    # El índice `i` inicia en 0
    # La cantidad de repeticiones es: repeticiones - 1 (en terminos de posicionamiento)
    print(f'Iteracion[{i}]: {mensaje}')