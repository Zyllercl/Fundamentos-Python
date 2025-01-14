'''
    OPERADORES DE ASIGNACION

    Def:
        - Los operadores de asignación se utilizan para asignar un valor a una variable y se utiliza el caracter '=':
            Ejemplo:
                - Sintaxis operador asignación:
                    variable = valor
        
        - En Python existe la asignación múltiple, es decir, permite asignar valores a varias variables en una sola línea de código. El código es más compacto y fácil de leer:
            Ejemplo:
                - Sintaxis de asignación multiple:
                    variable1, variable2 = valor1, valor2
        
        - En Python existe la asignación encadenada, es decir, permite asignar el mismo valor a múltiples variables:
            Ejemplo:
                - Sintaxis de asignación encadenada:
                    variable1 = variable2 = ... = valor
'''

'''     USO DE OPERADORES DE ASIGNACION    '''
# Ejemplo operador asignación
print(f'-----   Operador Asignación   -----')
numero = 1000
texto = 'Hola Mundo'
print(f'Variable Númerica: {numero}')
print(f'Variable Texto: {texto}\n')

# Ejemplo operador asignación múltiple
print(f'-----   Operador Asignación Múltiple   -----')
a, b, c = 'Hola', 100, 35.67
print(f'Variables Múltiples:\n a: {a}\n b: {b}\n c: {c}\n')

# Ejemplo operador asignación encadenada
print(f'-----   Operador Asignación Encadenada   -----')
contador1 = contador2 = 1
print(f'Variables Encadenadas:\n Contador1: {contador1}\n Contador2: {contador2}\n')

# Ejemplo de Intercambio de Valores de una variable (Sin utilizar Variables Temporales)
print(f'-----   Intercambio de Valores   -----')
x, y = 1, 5
print(f'Valores Originales\n X: {x}\n Y: {y}')
x,y = y, x
print(f'Variables Invertidas\n X: {x}\n Y {y}\n')

# Ingresar multiples valores de entrada
print(f'-----   Ingreso Multiples Valores   -----')
nombre, apellido = input('Ingrese su nombre y apellido (Separado por una coma): ').split(',')
print(f'Nombre: {nombre.strip()} , Apellido: {apellido.strip()}')
