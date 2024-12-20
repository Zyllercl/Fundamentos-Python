'''
    VALIDACION CAMPO DE UN FORMULARIO

    Def:
        - Validación para una variable que NO sea vacia hasta que el usuario rellene con data.
'''

print(f'-----   VALIDACION CAMPO DE UN FORMULARIO   -----')
# Variables
nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input('Ingresa tu nombre de usuario: ')

print(f'Nombre de usuario: {nombre_usuario}')