'''
    OPERADORES LOGICOS

    Def:
        - Los operadores lógicos se utilizan para realizar operaciones lógicas con valores booleados.
            Ejemplo:
                - Operador Lógico AND:  Devuelve 'True' si ambos oparendos son verdaderos

                                        TABLA DE LA VERDAD (AND)
                            |       a       |       b       |     a and b   |
                            |    False      |     False     |      False    |
                            |    False      |     True      |      False    |
                            |    True       |     False     |      False    |
                            |    True       |     True      |      True     |
                
                - Operador Lógico OR:   Devuelve 'True' si cualquiera de los operandos es verdadero

                                        TABLA DE LA VERDAD (OR)
                            |       a       |       b       |     a or b   |
                            |    False      |     False     |      False   |
                            |    False      |     True      |      True    |
                            |    True       |     False     |      True    |
                            |    True       |     True      |      True    |

                - Operador Lógico NOT:  Invierte el valor del operando (operador unario)

                                        TABLA DE LA VERDAD (NOT)
                                    |       a        |    not a    |
                                    |    False       |     True    |
                                    |    True        |     False   |
                                    
                    - Sintaxis Operador NOT
                        exp1 = False
                        print(not exp1) -> TRUE
'''

'''     USO DE OPERADORES LOGICOS   '''
# Operador Lógico AND
print(f'-----   Operador Lógico AND   -----')
condicion1 = False
condicion2 = True
resultado = (condicion1 and condicion2)
print(f'La condición {condicion1} and {condicion2}: {resultado}\n')

# Operador Lógico OR
print(f'-----   Operador Lógico OR   -----')
condicion1 = False
condicion2 = True
resultado = (condicion1 or condicion2)
print(f'La condición {condicion1} or {condicion2}: {resultado}\n')

# Operador Lógico NOT
print(f'-----   Operador Lógico NOT   -----')
condicion = False
resultado = not condicion
print(f'La condicion NOT {condicion} es: {resultado}\n')

nombre = ''
es_string_vacio = not nombre
print(f'La variable NO tiene ningún valor?: {es_string_vacio}')

variable = None
es_variable_sin_valor = not variable
print(f'La variable NO tienen ningún valor asignado?: {es_variable_sin_valor}')