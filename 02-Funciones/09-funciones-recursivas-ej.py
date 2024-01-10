
# Imprimir numeros de 5 a 1 de manera descendente
def valores_descendentes(numero):
    if numero >= 1:
        print(numero)
        valores_descendentes(numero - 1)
    elif numero == 0:
        return
    elif numero < 0:
        print('Numero negativo')


numero = 5
valores_descendentes(numero)