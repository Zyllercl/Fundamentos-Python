'''
    EJERCICIO ACUMULADOR SUMA

    Def: Realizar la suma de los primeros 5 números utilizando un ciclo while. Se debe sumar el primer numero con el segundo y posteriormente el resultado sumar con el numero siguiente y asi sucesivamente.
'''

print(f'-----   EJERCICIO ACUMULADOR SUMA   -----')
# Variables
MAXIMO = 5
numero = 1
acumulador = 0

while numero <= MAXIMO:
    # Imprime lo que se va acumulando
    print(f'La acumulacion de suma más el número es:  {acumulador} [Valor suma parcial] + {numero} [Valor contador]')

    acumulador += numero
    numero += 1

    # Imprime el resultado de la suma
    print(f'La suma acumulada es: {acumulador}\n')


print(f'La suma de los primeros {MAXIMO} números es: {acumulador}')
