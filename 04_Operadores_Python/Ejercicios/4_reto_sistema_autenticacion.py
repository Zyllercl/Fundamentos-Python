"""
RETO: Sistema de autenticación
==============================

Definición:
-----------

Crear un programa que valide el usuario y contraseña proporcionados por el usuario. Para ello, se deben definir dos constantes con los valores correctos y estos se deben comparar con los valores que ingresa el usuario por teclado. Si estos coinciden, entonces deberá imprimir True; de lo contrario, False.
"""

# ---------------------------
# Ejemplo de uso del operador AND
# ---------------------------
print(f'[RETO: SISTEMA DE AUTENTICACIÓN]\n')

# ---------------------------
# Variables constantes
# ---------------------------
USUARIO = 'root'
PASSWORD = 'toor'

# ---------------------------
# Entrada de datos
# ---------------------------
usuario = input('Cual es su usuario?: ')
password = input('Cual es tu contraseña?: ')

es_valido = (usuario.strip() == USUARIO) and (password.strip() == PASSWORD)

print(f'Datos correctos?: {es_valido}')