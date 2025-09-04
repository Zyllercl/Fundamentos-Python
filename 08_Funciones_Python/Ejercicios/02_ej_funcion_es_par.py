"""
Ejemplo: Verificar si un número es Par
======================================
Este script muestra la creación de un script para verificar si el número ingresado es par o no.
"""

print(f'[EJEMPLO] Función es_par')

# --------------------------
# Definicion de la funcion
# --------------------------
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# --------------------------
# Llamando a la funcion
# --------------------------
if __name__ == '__main__':
    numero = int(input('Ingresa un numero: '))

    print(f'Es número par?: {es_par(numero)}')
    