'''
    CALCULAR EL FACTORIAL DE UN NUMERO

    Def:
        - Crear una función recursiva para que calcule el factorial de un número.
'''

print(f'-----   CALCULAR EL FACTORIAL DE UN NUMERO  -----\n')

# Caso Base -> Factorial de  0! = 1
#           -> Factorial de  1! = 1

print(f'*** Factorial del número 5 ***')

# Funcion recursiva
def factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else:
        # Caso recursivo
        factorial_parcial = numero * factorial_recursivo(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')

        return factorial_parcial

numero = 5
resultado = factorial_recursivo(numero)

print(f'El factorial de {numero} es: {resultado}')
