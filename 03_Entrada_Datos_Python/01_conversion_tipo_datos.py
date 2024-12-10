'''
    CONVERSION DE TIPOS DE DATOS

    Def:
        - La conversión de tipos de datos conocida como 'Casting', sirve para manipular datos. Se puede realizar conversiones desde y hacia distintos tipos de datos.
            Ejemplo:
                - Convertir a Entero     -> Función int()
                - Convertir a Flotante   -> Función float()
                - Convertir a Cadena     -> Función str()
                - Convertir a Booleano   -> Función bool()
'''

'''     USO DE CONVERSION DE TIPOS DE DATOS    '''
# Conversión de Cadena a Número
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Conversion de String a Número: {numero_entero}')

# Conversión de Caneda a Flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Conversion de String a Flotante: {numero_flotante}')

# Conversión de Número a Cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Conversion de Número a String: {numero_cadena}')

# Conversión a Booleano
'''
    - Si el valor es 0, None o String vacio: Retornará un False
    - Si el valor es distinto de 0, None o String vacio: Retornará True
'''
numero_entero = 0
booleano = bool(numero_entero) # Return False
print(f'Conversión de Número 0 a Booleano: {booleano}') # False

numero_entero = 1
booleano = bool(numero_entero) # Return True
print(f'Conversión de Número 5 a Booleano: {booleano}') # True

cadena = ''
booleano = bool(cadena) # Return False
print(f'Conversión de String Vacio a Booleano: {booleano}') # False

cadena = 'String con Valor'
booleano = bool(cadena) # Return True
print(f'Conversión de String No Vacio a Booleano: {booleano}') # True

variable = None
booleano = bool(variable) # Return False
print(f'Conversión de None a Booleano: {booleano}') # False

