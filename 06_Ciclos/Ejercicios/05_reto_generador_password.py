"""
RETO: Creación y validación de contraseñas
==========================================

Definición:
-----------

Crear un programa para validar la creación de una contraseña. Para poder crear una contraseña se debe validar que:

    * La contraseña  debe tener al menos 6 caracteres *

En caso de no cumplir con esta condición el programa debe volver a solicitar un nuevo valor hasta que cumpla con la condición establecida.
Si el valor proporcionado es válido, se debe imprimir 'Password Válida' y debe terminar la ejecución del programa.
"""

print(f'[RETO] Creación y validación de contraseñas')

# Variable Globales
CARACTERES = 6

# Ingreso de datos: Contraseña
password = input('Crea una contraseña (Mínimo 6 caracteres): ')

# Validación del largo de la contraseña
while len(password) < CARACTERES:
    print('La contraseña ingresada no cumple con los requisitos.')
    password = input('Crea una contraseña válida: ')
else:
    print('Contraseña válida...')  
