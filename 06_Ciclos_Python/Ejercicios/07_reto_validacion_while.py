"""
RETO: Validación campo de un formulario
=======================================

Definición:
-----------

Crea un programa que valide el ingreso de un nombre de usuario. El programa debe funcionar de la siguiente manera:

    1. Solicita al usuario que ingrese su nombre de usuario.
    2. Si el usuario ingresa una cadena vacía (es decir, no ingresa nada y presiona Enter), el programa debe seguir solicitando el nombre de usuario hasta que se ingrese un valor válido (una cadena no vacía).
    3. Una vez que se ingrese un nombre de usuario válido, el programa debe imprimir el nombre de usuario y finalizar.
"""

print(f'[RETO] Validación campo de un formulario')

# Variables Locales
nombre_usuario = None

# Validación del nombre de usuario que no sea vacío
while not nombre_usuario:
    nombre_usuario = input('Ingresa tu nombre de usuario: ')

print(f'Nombre de usuario: {nombre_usuario}')