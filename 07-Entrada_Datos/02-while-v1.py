
# While en Python

"""
    For     -> Se ejecuta determinado número de ocasiones según sean los elementos de un arreglo
    While   -> Se ejecuta mientras una condición sea verdadera
"""

pregunta = 'Agrega un numero y te dire si es par o impar '
pregunta += '(Escribe "cerrar" para salir de la aplicacion): '

preguntar = True

while preguntar:
    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print(f'El numero {numero} es par')
        else:
            print(f'El numero {numero} es impar')