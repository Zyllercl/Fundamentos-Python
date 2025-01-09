'''
    SUMA CON ARGUMENTOS VARIABLES

    Def:
        - Crear una función para que acepte argumentos variables y posteriormente realizar la suma de los valores ingresados.
'''

print(f'-----   SUMA CON ARGUMENTOS VARIABLES  -----')

# Funcion
def sumar_args_variables(*args):
    total = 0

    for numero in args:
        total += numero
    
    return total

# Llamando a la funcion
resultado = sumar_args_variables(1, 2, 3, 4, 5)
print(f'Resultado de la suma: {resultado}')