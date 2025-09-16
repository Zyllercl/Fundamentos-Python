"""
Módulos en Python
=================
En este script contiene la función `sumar()`, la cual recibe dos valores como argumentos y devuelve su suma.

Para poder realizar "pruebas internas" dentro del mismo archivo, sin que se ejecuten ciando el módulo sea importado desde otro archivo, se utiliza la siguiente estructura:

    if __name__ == '__main__':
        # Bloque de código de pruebas
"""

# ----------------------------
# Definición de la función suma()
# ----------------------------
def sumar(a, b):
    resultado = a + b

    return resultado

# ----------------------------
# Prueba de la función
# ----------------------------
if __name__ == '__main__':
    print(f'Prueba de la función sumar: {sumar(10, 17)}')