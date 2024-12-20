'''
    CREACIÓN Y VALIDACION DE CONTRASEÑAS

    Def:
        - Crear un programa para validar la creación de una contraseña. Para poder crear una contraseña se debe validar que:
            
            * La contraseña  debe tener al menos 6 caracteres *
        
        - En caso de no cumplor con esta condición el programa debe volver a solicitar un nuevo valor hasta que cumpla con la condición establecida.
        - Si el valor proporcionado es válido, se debe imprimir 'Password Válida' y debe terminar la ejecución del programa.
'''

print(f'-----   CREACIÓN Y VALIDACION DE CONTRASEÑASE   -----')
# Variables
CARACTERES = 6

password = input('Crea una contraseña (Minimo 6 caracteres): ')

while len(password) < CARACTERES:
    print('La contraseña ingresada no cumple con los requisitos.')
    password = input('Crea una contraseña válida: ')
else:
    print('Contraseña válida...')  
