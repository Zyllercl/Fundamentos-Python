'''
    OPERADORES CONDICIONALES

    Def:
        - Los operadores condicionales se utilizan para comparar dos valores. El resultado siempre es un valor booleano 'True' o 'False', dependiendo de si la condición se cumple o no.
            Ejemplo:
                - Operador de Igualdad (==):   Compara si dos valores son iguales
                    - Sintaxis operador igualdad 
                            a == b
                
                - Operador distinto (!=):   Compara si dos valores son distintos
                    - Sintaxis operador distinto
                            a != b
                
                - Operador menor que (<):   Compara si el valor de la izquierda es MENOR que el de la derecha devuelve TRUE, sino FALSE
                    - Sintaxis operador menor que
                            a < b
                
                - Operador menor o igual que (<=):  Verifica si el valor de la izquierda es MENOR O IGUAL al valor de la derecha devuelve TRUE, sino FALSE
                    - Sintaxis operador menor o igual que
                            a <= b
                
                - Operador mayor que (>):   Compara si el valor de la izquierda es MAYOR que el de la derecha devuelve TRUE, sino FALSE
                    - Sintaxis operador mayor que
                            a > b
                
                - Operador mayor o igual que (>=):  Verifica si el valor de la izquierda es MAYOR O IGUAL al valor de la derecha devuelve TRUE, sino FALSE
                    - Sintaxis operador mayor o igual que
                            a >= b
'''

'''     USO DE OPERADORES CONDICIONALES   '''
# Variables
a, b = 7, 2
print(f'Variables Iniciales:\n a: {a}\n b: {b}')

# Operador de Igualdad ( == )
print(f'-----   Operador de Igualdad   -----')
resultado = (a == b)
print(f'Resultado a == b es: {resultado}\n')

# Operador Distinto ( != )
print(f'-----   Operador Distinto   -----')
resultado = (a != b)
print(f'Resultado a != b es: {resultado}\n')

# Operador Menor que ( < )
print(f'-----   Operador Menor que   -----')
resultado = (a < b)
print(f'Resultado a < b es: {resultado}\n')

# Operador Menor o igual que ( <= )
print(f'-----   Operador Menor o Igual que   -----')
resultado = (a <= b)
print(f'Resultado a <= b es: {resultado}\n')

# Operador Mayor que ( > )
print(f'-----   Operador Mayor que   -----')
resultado = (a > b)
print(f'Resultado a > b es: {resultado}\n')

# Operador Mayor o igual que ( >= )
print(f'-----   Operador Mayor o Igual que   -----')
resultado = (a >= b)
print(f'Resultado a >= b es: {resultado}\n')