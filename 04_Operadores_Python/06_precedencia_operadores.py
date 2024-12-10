'''
    PRECEDENCIA DE OPERADORES

    Def:
        - La precedencia de operadores determina el orden en que se evalúan las operaciones en una expresión.

        - Python aplica la siguiente tabla para asegurar que algunos operadores tengan mayor prioridad que otros durante la evaluacion de expresiones:

            1.- Operador paréntesis     -> ()
            2.- Exponente               -> **
            3.- Unarios                 -> +x , -x
            4.- Multi,Div,Modulo        -> * , / , // , %
            5.- Suma y resta            -> + , -
            6.- Comparación             -> == , != , < , <= , > , >=
            7.- Operadores Lógicos      -> not , and , or
            8.- Operadores Asignación   -> = , += , -= , /= , //= , **=
'''

'''     USO DE PRECEDENCIA DE OPERADORES    '''
resultado = 12 / 3 + 2 * 3 - 1
print(f'Resultado: {resultado}')

# Desglose del ejercicio
# 1.- Division: 12 / 3          -> 4
# 2.- Multiplicacion: 2 * 3     -> 6
# 3.- Suma: 4 + 6               -> 10
# 4.- Resta: 10 - 1             -> 9 Valor Final