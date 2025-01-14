'''
    FORMATEO DE STRINGS

    Def:
        - Python incluye varias maneras de concatenar cadenas, variables e incluso dar otro tipo de formateo.
            Ejemplos:
                - Uso de f-string       # Formas mas eficiente de concatenar strings.
                - Uso de método format  # Permite construir cadenas complejas.
'''

'''     USO DE FORMATEO DE STRINGS    '''
# Uso de f-string
variable = "Mundo"
resultado = f'Hola {variable}'
print(resultado)

# Uso de Método Format
variable = "Mundo"
resultado = 'Adios {}'.format(variable)
print(resultado)