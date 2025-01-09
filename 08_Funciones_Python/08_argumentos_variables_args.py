'''
    ARGUMENTOS VARIABLES 

    Def:
        - Los argumentos variables permiten que una función acepte un número arbitrario de elementos. Hay dos tipos principales: 
        
            1. Argumentos Posicionales Variables ( *args ):   Permite pasar múltiples argumentos posicionales a una función, recibiendolos como una tupla dentro de la función. Cabe destacar que entregar parametros a ' *args ' es opcional.

                *args   -> Argumentos en forma de Tupla
'''

print(f'-----   ARGUMENTOS VARIABLES   -----')

# Funcion
def superheroe_superpoderes(superheroe, nombre, *args):
    # El parametro *args se tomará como los 'superpoderes', es decir, que puede tener 1 o más en forma de tupla.
    print(f'\nSuperheroe: {superheroe} - {nombre} - {args}')

    # Iterar la tupla de *args (Superpoderes)
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')


# Llamando a la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Telaraña', 'Instinto Arácnido')
superheroe_superpoderes('Iron Man', 'Tony Stark', 'Armadura', 'Millonario', 'Volar')

# No entregar argumentos variables *args (Opciona)
superheroe_superpoderes('Guardianes de la Galaxia', 'Groot')