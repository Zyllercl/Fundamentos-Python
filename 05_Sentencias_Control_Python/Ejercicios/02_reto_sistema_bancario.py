"""
RETO: Sistema Bancario
======================

Definición:
-----------

Crear un programa que simule un sistema bancario, donde se solicite al usuario si desea continuar dentro del sistema o salir. Utilizar el operador 'not' para aplicar la lógica inversa y considerar los siguientes puntos:

    1. Si NO desea salir del sistema, imprimir: 'Continuamos dentro del sistema...'
    2. De lo contrario, imprimir: 'Saliendo del sistema...'
"""

# -----------------------------
# Ejemplo de sistema bancario
# -----------------------------
print(f'[SISTEMA BANCARIO]\n')

# -----------------------------
# Solicitar si desea salir del sistema
# -----------------------------
salida_sistema = input('Deseas salir del sistema? (Si/No): ')

# -----------------------------
# Validar si desea salir del sistema
# -----------------------------
salir_del_sistema = salida_sistema.strip().lower() == 'si'

# -----------------------------
# Aplicar lógica inversa con 'not'
# -----------------------------
if not salir_del_sistema:
    print('Continuamos dentro del sistema...')
else:
    print('[!] Saliendo del sistema...')