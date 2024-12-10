'''
    GENERAR NUMEROS ALEATORIOS

    Def:
        - La función randint() es parte de un módulo 'random' que permite generar números aleatorios.
        - Para usar esta función, se debe importar el módulo, para ello se usa la siguiente sintaxtis:
            -   import random               -> Importa todos los metodos y funciones de random
            -   from random import randint  -> Importa sólo la funcion randint()

            Ejemplo:
                - randint(a,b)  -> Devuelve un número aleatorio entre 'a' y 'b', incluyendo estos valores.
        
'''

'''     USO DE RANDOM (NUMEROS ALEATORIOS)    '''
from random import randint

num_aleatorio = randint(1,10)
print(f'Numero aleatorio (entre 1 y 10): {num_aleatorio}')

'''     SIMULACIÓN DE UN DADO    '''
dado = randint(1,6)
print(f'Resultado al lanzar el dado: {dado}')