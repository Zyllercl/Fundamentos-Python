'''
    OPERADORES ARITMETICOS

    Def:
        - Los operadores aritméticos permiten realizar cálculos matemáticos básicos entre números como:
            
            - Suma  (+):            Suma de dos operandos.
            - Resta (-):            Resta de dos operandos.
            - Multiplicacion (*):   Múltiplica dos operandos.
            - Disivión  (/):        Divide el primer operando entre el segundo (Tipo Flotante).
            - División Entera (//): Divide el primer operando entre el segundo (Tipo Entero).
            - Módulo (%):           Regresa el residuo de una división.
            - Exponente (**):       Eleva el primer operando a la potencia del segundo.
'''

'''     USO DE OPERADORES ARITMETICOS    '''
# Variables
a = 16
b = 3

# Operador Suma
suma = a + b
print(f'Suma: {suma}')

# Operador Resta
resta = a - b
print(f'Resta: {resta}')

# Operador Multiplicador
multiplicacion = a * b
print(f'Multiplicacion: {multiplicacion}')

# Operador Division (2 decimales)
division = a / b
print(f'Disivion: {division:.2f}')

# Operador Division Entera
division_entera = a // b
print(f'Division entera: {division_entera}')

# Operador Módulo
modulo = a % b
print(f'Residuo disivion: {modulo}')

# Operador Potencia
potencia = a ** b # A elevado a B
print(f'Potencia: {potencia}')