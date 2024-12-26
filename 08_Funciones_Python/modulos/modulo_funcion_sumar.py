'''
    MODULOS EN PYTHON

    - Para realizar pruebas de las funciones creadas en un módulo y que no se ejecuten cuando se manda a llamar una función se debe definir la siguiente estructura:

        if __name__ == '__main__':
            # Bloque de codigo
        
        - Al momento de llamar una función desde otro archivo, todo lo que se encuentre dentro del bloque de código no se ejecutará fuera de este archivo.
'''

# Definicion de la funcion
def sumar(a, b):
    resultado = a + b
    return resultado


# Prueba de la función
if __name__ == '__main__':
    print(f'Prueba de la función sumar: {sumar(10, 17)}')