"""
RETO: Mayor de 2 Números
========================

Definición:
-----------

Crear un programa para indicar cual es el mayor de 2 números. El usuario debe ingresar dos números enteros para comparar y mandar a imprimir el número mayor.
"""

print(f'[RETO MAYOR DE 2 NÚMEROS]\n')

# -----------------------------
# Solicitar números al usuario
# -----------------------------
numero_1 = int(input('Ingrese un número entero positivo: '))
numero_2 = int(input('Ingrese un número entero positivo: '))

# -----------------------------
# Comparar los números y determinar el mayor
# -----------------------------
if numero_1 > numero_2:
    print(f'El número mayor es: {numero_1}')
else:
    print(f'El número mayor es: {numero_2}')