
# Funcion Recursiva -> Es una funcion que se vuelva a llamar

# Funcion Factorial
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = 3
resultado = factorial(numero)

print(f'El factorial de {numero} es: {resultado}')
