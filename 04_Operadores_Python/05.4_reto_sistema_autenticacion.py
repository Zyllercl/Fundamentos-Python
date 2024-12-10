'''
    SISTEMA DE AUTENTICACION

    Def:
        - Crear un programa para validar el usuario y contraseña proporcionados por el usuario. Para ello, se debe crear 2 constantes con los valores correctos y estos se deben comprar con los valores que ingresa el usuario por teclado, si estos coinciden, entonces debera imprimir True, de lo contrario False.
'''

print(f'-----   SISTEMA DE AUTENTICACION   -----')
# Variables
USUARIO = 'root'
PASSWORD = 'toor'

usuario = input('Cual es su usuario?: ')
password = input('Cual es tu contraseña?: ')

es_valido = (usuario.strip() == USUARIO) and (password.strip() == PASSWORD)

print(f'Datos correctos?: {es_valido}')