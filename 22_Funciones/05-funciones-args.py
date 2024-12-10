
# Sumar varios numeros con la funcion *args
def sumar(*args):
    resultado = 0

    for valor in args:
        resultado += valor
    return resultado

print(f'La suma es: {sumar(3, 7, 5)}')

# Multiplicar varios numeros con la funcion *args
def multiplicar(*args):
    resultado = 1

    for valor in args:
        resultado *= valor
    return resultado

print(f'La multiplicacion es: {multiplicar(3, 7, 5)}')