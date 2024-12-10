'''
    CONCATENACION DE STRINGS

    Def:
        - La concatenación de strings permite combinar dos o más cadenas para formar una nueva cadena.
            Ejemplos:
                - Operador +        # Concatenación directa al momento de agregar un + entre dos string
                - Operador JOIN     # Permite unir tantas cadenas sea necesario. Se necesita pasar cada string a concatenar separado por coma y entre parentesis
'''

'''     USO DE CONCATENACION    '''
# Operador +
string_1 = "Hola"
string_2 = "Mundo"
concatenacion = string_1 + ' ' + string_2
print('Uso de Operador +:', concatenacion)

# Operador JOIN
concatenacion = ''.join([string_1, ' ', string_2])
print('Uso de Operador JOIN:', concatenacion)
