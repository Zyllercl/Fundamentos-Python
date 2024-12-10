'''
    METODOS DE STRINGS

    Def:
        - Los strings en Python vienen con métodos utiles que facilitan su manipulación.
            Ejemplos:
                - Uso de upper():   Cambia las letras a mayúsculas.
                - Uso de lower():   Cambia las letras a minúsculas.
                - Uso de strip():   Elimina espacios en blanco al inicio y al final de una cadena.
                - Uso de len():     Obtener el largo de una cadena, tambien funciona para cadenas, listas, etc.
'''

'''     USO DE METODOS DE STRINGS    '''
variable_original = 'Hola Mundo'
print(f'Variable Original: {variable_original}')

# Método upper()
mayusculas = variable_original.upper()
print(f'Uso de Upper: {mayusculas}')

# Método lower()
print(f'Uso de Lower: {variable_original.lower()}')

# Méteodo Strip()
variable_editada = '    Hola Mundo'
print(f'Variable Editada: {variable_editada}')
print(f'Uso de Strip: {variable_editada.strip()}\n')

# Método len()
cadena_original = 'Hola, Mundo!'
print(f'String Original: {cadena_original}')
print(f'Largo del string: {len(cadena_original)}')