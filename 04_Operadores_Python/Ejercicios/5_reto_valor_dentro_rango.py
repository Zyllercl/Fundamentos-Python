"""
RETO: Valor dentro de rango
===========================

Definición:
-----------

Crear un programa que solicite al usuario ingresar un valor entre 0 y 5 e indicar si el valor está dentro del rango. Imprimir True si está dentro del rango, de lo contrario False. Para ello se deben definir 2 constantes:

- VALOR_MINIMO = 0
- VALOR_MAXIMO = 5
"""

# ---------------------------
# Ejemplo de uso del operador de comparación
# ---------------------------
print(f'[RETO: VALOR DENTRO DE RANGO]\n')

# ---------------------------
# Variables constantes
# ---------------------------
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

# ---------------------------
# Entrada de datos
# ---------------------------
numero = int(input('Ingrese un número entero: '))

# ---------------------------
# Validación del rango
# ---------------------------
resultado = (VALOR_MINIMO <= numero <= VALOR_MAXIMO)

print(f'El numero {numero} se encuentra entre {VALOR_MINIMO} y {VALOR_MAXIMO}?: {resultado}')