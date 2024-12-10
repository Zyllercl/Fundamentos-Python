'''
    CADENAS EN PYTHON

    Def:
        - Una cadena o 'string' es un tipo de dato que se utiiza para almacenar una secuencia de caracteres.
        - Las cadenas se deben encerrar entre comillas dobles o simples.
        - Los caracteres puede ser letras, números, símbolos o espacios.

    Detalle de un String:
        - Los caracteres de una cadena están indexados de manera secuencial, es decir, que se puede acceder a cada caracter indicando el índice del caracter que se quiere visualizar.
            Ejemplo:
                - detalle_frase = "Obteniendo un caracter"
                    print(detalle_frase[0])     # Recuperar el primer caracter 'O'
                    print(detalle_frase[-1])    # Recuperar el último caracter 'r'
                    print(detalle_frase[0:5])   # Recuperar varios caracteres, es decir, de la posición 0 hasta la posicion 5


    Inmutabiliidad de un String:
        - Cuando se declara una variable de tipo String, los caracteres dentro de ella no pueden ser modificados. Si se desea modificar una cadena, se debe crear una nueva cadena.
            Ejemplo:
                - frase_1 = "Hola Mundo"
                    frase_1[0] = "h"  <- [ERROR] No se puede cambiar un caracter de un string. Tipo Error: 'str' object does not support item assignment
'''

'''     USO DE STRING    '''
# Sintaxis de String
frase_1 = "Hola Mundo"
frase_2 = "Adiós Mundo"
frase_3 = '''Mensaje con
saltos de linea y
    tabulación incluida
'''

'''     RE-ASIGNACION DE STRING    '''
frase_2 = frase_1   # Reemplazo de cadena de la frase_2 por la cadena de la frase_1
frase_1 = "Mundo"   # Reemplazo de cadena de la frase_1 a otra cadena

print('frase_2 cambiada a:', frase_2)
print('frase_1 cambiada a:', frase_1)