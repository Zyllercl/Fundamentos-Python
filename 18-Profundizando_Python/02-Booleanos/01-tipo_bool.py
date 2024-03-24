# Booleano en Python Avanzado

""" 
    Bool -> Tiene 2 valores (True | False)
    
    Tipo numerico:
        0               -> False
        Mayores a 0     -> True
    
    Tipo string:
        ''                  -> False
        'cualquier_texto'   -> True
"""

#   Tipo Numerico   #
# print(f'[Bool] Tipo Numerico')

# Booleano False
valor = 0
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Booleano True
valor = 1
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

#   Tipo String     #
# print(f'[Bool] Tipo String')

# Booleano False
valor = ''
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Booleano True
valor = 'test'
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

#   Tipo Lista      #
# print(f'[Bool] Tipo Lista')

# Booleano False
valor = []
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Booleano True
valor = [1,2,3]
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

#   Tipo Tupla      #
# print(f'[Bool] Tipo Tupla')

# Booleano False
valor = ()
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Booleano True
valor = (1,2,3)
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

#   Tipo Diccionario    #
# print(f'[Bool] Tipo Diccionario')

# Booleano False
valor = {}
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Booleano True
valor = {
    'username': 'mopa',
    'password': 'chino'
}
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')


#   Sentencias de control   #

variable = 0

# Conversion explicita a booleano
if bool(variable):
    print('True')
else:
    print('False')

# Conversion no explicita a booleano
if variable:
    print('True')
else:
    print('False')


while variable:
    print('Ejecucion ciclo while')
    break
else:
    print('Fin ciclo while')