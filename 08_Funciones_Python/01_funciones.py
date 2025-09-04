"""
Funciones en Python
==================================
Este script muestra un ejemplo básico de como declarar una función con y sin parámetros.
"""

print(f'[FUNCION SIN PARAMETRO]\n')

# -----------------------
# Definición de una función (sin parametros)
# -----------------------
def saludar():
    # Cuerpo de la funcion
    print('Hola mundo!')

# -----------------------
# Llamar a una función (Programa Principal)
# -----------------------
saludar()

# --------------------------------------

print(f'\n[FUNCION CON PARAMETRO]\n')

# -----------------------
# Definición de una función (con parametros)
# -----------------------
def saludar(mensaje):
    # Cuerpo de la funcion
    print(f'Mensaje enviado: {mensaje}')

# Llamar a una función (Programa Principal)
saludar('Esto es un mensaje pasado por parámetro...')