'''
    DETALLE DE PERSONAS CON ARGUMENTOS VARIABLES

    Def:
        - Crear una función para que acepte argumentos variables en forma de llave - valor (Diccionario).
'''

print(f'-----   DETALLE DE PERSONAS CON ARGUMENTOS VARIABLES  -----')

# Funcion
def detalle_persona(**kwargs):
    print('\nValores Recibidos')

    for llave, valor in kwargs.items():
        print(f'{llave} : {valor}')
    
# Llamamos a la funcion
detalle_persona(nombre = 'Octavia', apellido = 'Blake', edad = 29)
detalle_persona(nombre = 'Bellamy', apellido = 'Blake', edad = 32)
