"""
Ejemplo: Funcion sumar
======================
Este script muestra un ejemplo de como una funcion para realizar una suma.
"""
print(f'[EJEMPLO] Función Sumar\n')

# --------------------------
# Definicion de la funcion
# --------------------------
def sumar(a, b):
    resultado = a + b
    return resultado

# --------------------------
# Llamar a la funcion
# --------------------------
resultado_funcion = sumar(5, 7) # Ejemplo 1
print(f'Resultado de la suma (5 + 7): {resultado_funcion}\n')

resultado_funcion = sumar(5, 75) # Ejemplo 2
print(f'Resultado de la suma (5 + 75): {resultado_funcion}')