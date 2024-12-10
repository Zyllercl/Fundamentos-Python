'''
    OPERADORES DE ASIGNACION COMPUESTOS

    Def:
        - Los operadores de asignación compuestos combinan una operación aritmética con una asignación.
            Ejemplo:
                - Sintaxis operador asignación compuestos:
                    variable OPERADOR= valor
'''

'''     USO DE OPERADORES DE ASIGNACION COMPUESTOS    '''
# Variables
a, b = 7, 2
print(f'Variables Iniciales:\n a: {a}\n b: {b}')

# Operador Compuesto de Suma ( += )
print(f'-----   Operador Compuesto Suma   -----')
a += b
print(f'Operador compuesto a += b es: {a}\n')

# Operador Compuesto de Resta ( -= )
print(f'-----   Operador Compuesto Resta   -----')
a -= b
print(f'Operador compuesto a -= b es: {a}\n')

# Operador Compuesto de Multiplicación ( *= )
print(f'-----   Operador Compuesto Multiplicación   -----')
a = 9
a *= b
print(f'Operador compuesto a *= b es: {a}\n')

# Operador Compuesto de División ( /= )
print(f'-----   Operador Compuesto División   -----')
a = 7
a /= b
print(f'Operador compuesto a /= b es: {a:.2f}\n')