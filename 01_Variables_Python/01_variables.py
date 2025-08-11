"""
Uso de Variables en Python
==========================
Este script demuestra:
- Cómo declarar y asignar  valores a variables.
- Cómo acceder y modificar sus valores.
- Reglas y convenciones para nombres en Python.
"""

# Ejemplo básico: declaración y valor de una variable
nombre_de_la_variable = 'valor'
print('Posición de Memoria:', id(nombre_de_la_variable))

# ------------------------------
# Declaración de variables
# ------------------------------
nombre = "Pepe"         # str:  Texto
edad = 18               # int:  Entero
peso = 70.4             # float: Número decimal
es_casado = False       # Bool: Verdadero/Falso

# Mostrar valores originales
print('\nValores Originales')
print('Nombre:', nombre)
print('Edad:', edad)
print('Peso:', peso)
print('Casado:', es_casado)

# ------------------------------
# Modificación de variables
# ------------------------------
nombre = "Pepito Jr"
edad = 10

print('\nValores Modificadas')
print('Nombre:', nombre)
print('Edad:', edad)

# ------------------------------
# Reglas y convenciones
# ------------------------------
print('\nReglas y Convenciones')

nombre_usuario = "Usuario 1" # snake_case: Recomendado

# ❌ Ejemplos inválidos:
# 1nombre_usuario = "Usuario 1" -> [ERROR] No se puede crear una variable con un numero al principio.
# class = "Usuario"             -> [ERROR] No se puede usar palabras reservadas.

# Python distingue entre mayúsculas y minúsculas (case-sensitive)
nombre = "Usuario 1"
Nombre = "Usuario 2"
print('La variable "nombre" es:', nombre, ', es diferente de "Nombre":', Nombre)

# Prefijos y Subfijos en nombres de variables
es_casado = False           # Prefijo "es_" sugiere que es un valor booleano.
nombre_txt = "archivo.txt"  # Sufijo "_txt" indica el tipo de dato o formato.