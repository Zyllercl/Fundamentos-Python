'''
    VERIFICAR SI UN NUMERO ES PAR

    Def:
        - Crear una función para saber si el número es par o no
'''

print(f'-----   VERIFICAR SI UN NUMERO ES PAR  -----')

# Funcion
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Llamando a la funcion
if __name__ == '__main__':
    numero = int(input('Ingresa un numero: '))

    print(f'Es número par?: {es_par(numero)}')
    