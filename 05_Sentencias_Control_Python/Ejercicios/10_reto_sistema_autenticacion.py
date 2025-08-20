"""
RETO: Sistema de Autenticación
==============================

Definición:
-----------

Crear un programa para validar los valores de usuario y password ingresados por consola. Se deben definir 2 constantes con los valores válidos de usuario y password.

El programa debe comparar los valores validos contra los valores ingresados por teclado, se debe considerar los siguientes puntos:

    1. Usuario y Password válidos: Deberá imprimir 'Bienvenido al Sistema'
    2. Usuario Invalido
    3. Password Invalido
    4. Usuario y Password invalidos
"""

print(f'[SISTEMA DE AUTENTICACIÓN]\n')

# -----------------------------
# Definir constantes para usuario y password válidos
# -----------------------------
USUARIO_VALIDO = 'root'
PASSWORD_VALIDA = 'toor'

# -----------------------------
# Solicitar usuario y password al usuario
# -----------------------------
usuario = input('Usuario: ').strip()
password = input('Contraseña: ').strip()

# -----------------------------
# Validar usuario y password
# -----------------------------
if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDA:
    print(f'[+] Bienvenido, autentificación éxitosa.')
elif usuario != USUARIO_VALIDO and password != PASSWORD_VALIDA:
    print(f'[-] Error usuario y contraseña no válido!')
elif usuario != USUARIO_VALIDO:
    print(f'[!] Error usuario no válido!')
elif password != PASSWORD_VALIDA:
    print(f'[!] Error contraseña no válido!')
