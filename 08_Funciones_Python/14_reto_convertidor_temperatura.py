'''
    CONVERTIDOR DE TEMPERATURA

    Def:
        - Crear una funcion que permita calcular la temperatura de Celsius a Fahrenheit y viceversa 
'''

print(f'-----   CONVERTIDOR DE TEMPERATURA   -----')

# Funcion de Celsius a Fahrenheit


# Funciopn de Fahrenheit a Celsius
def celsius_fahrenheit(celsius):
    fahrenheit = celsius *  9 / 5 + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Conversion de grados Celsius a Fahrenheit
valor_celsius = int(input('Ingrese los grados C°: '))
resultado_celsius = celsius_fahrenheit(valor_celsius)
print(f'C° a F° es: {resultado_celsius}')

# Conversion de grados Fahrenheit a Celcius
valor_fahrenheit = int(input('Ingrese los grados F°: '))
resultado_fahrenheit = fahrenheit_celsius(valor_fahrenheit)
print(f'F° a C" es: {resultado_fahrenheit}')
