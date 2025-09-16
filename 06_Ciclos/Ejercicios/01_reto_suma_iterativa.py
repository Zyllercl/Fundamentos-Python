"""
RETO: Ejercicio con ciclo while
===============================

Definición:
-----------

Realizar un ciclo 'while' que sume los primeros 5 números e imprima el resultado en cada iteración.
"""

print(f'[RETO] Ejercicio con ciclo WHILE - Suma iterativa\n')

# Variables Globales
MAXIMO = 5

# Variables Locales
numero = 1
acumulador = 0

# ---------------------
# Ciclo WHILE para sumar los primeros 5 números
# ---------------------
while numero <= MAXIMO:
    # Imprime lo que se va acumulando
    print(f'La acumulacion de suma más el número es: {acumulador} [Valor suma parcial] + {numero} [Valor contador]')

    acumulador += numero # Realiza el incremento del acumulador
    numero += 1          # Incremento del número

    # Imprime la suma acumulada en cada iteración
    print(f'La suma acumulada es: {acumulador}\n')

# Imprime el resultado final
print(f'La suma de los primeros {MAXIMO} números es: {acumulador}')
