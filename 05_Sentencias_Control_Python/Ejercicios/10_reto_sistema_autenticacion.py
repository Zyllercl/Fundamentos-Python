'''
    SISTEMA DE AUTENTICACION

    Def:
        - Crear un programa para validar los valores de usuario y password ingresados por consola. Se deben definir 2 constantes con los valores válidos de usuario y password.

        - El programa debe comparar los valores validos contra los valores ingresados por teclado, se debe considerar los siguientes puntos:
            
            1.- Usuario y Password válidos: Deberá imprimir 'Bienvenido al Sistema'
            2.- Usuario Invalido
            3.- Password Invalido
            4.- Usuario y Password invalidos
'''

print(f'-----   SISTEMA DE AUTENTICACION   -----')
# Variables
usuario_valido = 'root'
password_valida = 'toor'

usuario = input('Usuario: ').strip()
password = input('Contraseña: ').strip()

if usuario == usuario_valido and password == password_valida:
    print(f'[+] Bienvenido, autentificación éxitosa.')
elif usuario != usuario_valido and password != password_valida:
    print(f'[-] Error usuario y contraseña no válido!')
elif usuario != usuario_valido:
    print(f'[!] Error usuario no válido!')
elif password != password_valida:
    print(f'[!] Error contraseña no válido!')
