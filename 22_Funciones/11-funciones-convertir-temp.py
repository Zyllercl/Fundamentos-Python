
# Crear dos funciones que devuelvan la temperatura de C a F y vivecersa

def celsius_fahrenheit(celsius):
    # Formula
    formula = celsius * 9/5 + 32
    return formula

def fahrenheit_celsius(fahrenheit):
    # Formula
    formula = (fahrenheit - 32) * 5 / 9
    return formula

# Celsius a Fahrenheit
celsius = float(input('Ingrese temp en Celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F: {resultado:.2f} F')

# Fahrenheit a Celsius
fahrenheit = float(input('Ingrese temp en Fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C: {resultado:.2f} C')