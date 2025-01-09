'''
    ARGUMENTOS VARIABLES 

    Def:
        - Los argumentos variables permiten que una función acepte un número arbitrario de elementos. Hay dos tipos principales: 

            1. Argumentos con Palabra Clave ( **kwargs ):   Recibe los argumentos en forma de diccionario (llave - valor). Cabe destacar que entregar parametros a ' **kwargs ' es opcional.

                **kwargs   -> Keyword Arguments (key, value) en forma de Diccionario
'''

print(f'-----   ARGUMENTOS VARIABLES   -----')

# Funcion
def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')


# Llamada a la funcion
superheroe_superpoderes('Spiderman', 'Instinto Aracnido', edad = 27, empresa = 'Marvel')
superheroe_superpoderes('Iron Man', 'Armadura', 'Volar', edad = 38)