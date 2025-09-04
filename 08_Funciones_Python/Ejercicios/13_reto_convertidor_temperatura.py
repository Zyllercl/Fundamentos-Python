"""
RETO: Convertidor de Temperatura
================================

Definición:
-----------

Crear una función que permita calcular la Temperatura de Celsius a Fahrenheit y Viceversa.
"""

print(f'[RETO] Convertidor de Temperatura\n')

# --------------------------------------
# Función de Celsius a Fahrenheit
# --------------------------------------
def celsius_fahrenheit(celsius):
    fahrenheit = celsius *  9 / 5 + 32
    return fahrenheit

# --------------------------------------
# Función de Fahrenheit a Celsius 

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# --------------------------------------
# T° de C° a F°
# --------------------------------------
valor_celsius = int(input('Ingrese los grados C°: '))
resultado_celsius = celsius_fahrenheit(valor_celsius)
print(f'C° a F° es: {resultado_celsius}\n')

# --------------------------------------
# T° de F° a C°
# --------------------------------------
valor_fahrenheit = int(input('Ingrese los grados F°: '))
resultado_fahrenheit = fahrenheit_celsius(valor_fahrenheit)
print(f'F° a C" es: {resultado_fahrenheit}')
