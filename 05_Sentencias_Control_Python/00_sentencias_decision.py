'''
    SENTENCIAS DE DECISION

    Def:
        - Las sentencias de decisión permiten controlar el fluo de ejecución de un programa. Existen diferentes sentencias de decisión como:

            - Sentencia 'if':   Permite ejecutar un bloque de código si la condición a evaluar es verdadera. Una condición es una expresión que evalua con True o False.
                Ejemplo:
                    - Sintaxis sentencia if
                        if condicion: 
                            # Bloque de código que se ejecuta si la condición es True

            - Sentencia 'if else': Permite ejecutar un bloque de código cuando la condición del 'if' es falsa (False).
                Ejemplo:
                    - Sintaxis sentencia if else
                        if condicion:
                            # Bloque de código que se ejecuta si la condición es True
                        else:
                            # Bloque de código que se ejecuta si la condición es False
            
            - Sentencia 'if elif else': Abreviatura de 'elif' es 'else if', se utiliza para verificar múltiples condiciones, una tras otra.
                Ejemplo:
                    - Sintaxis sentencia if elif else
                        if condicion1:
                            # Bloque de código que se ejecuta si la condición1 es True
                        elif condicion2:
                            # Bloque de código que se ejecuta si la condición2 es True 
                        else:
                            # Bloque de código que se ejecuta si las condiciones son False
'''

'''     USO DE SENTENCIA DE DESICION    '''
# Ejemplo sentencia if
print(f'-----   SENTENCIA IF   -----')
edad = 30
if edad >= 21:
    print(f'+ Cumples la mayoría de edad con {edad} años\n')

# Ejemplo sentencia if else
print(f'-----   SENTENCIA IF ELSE   -----')
edad = 15
if edad >= 21:
    print(f'+ Cumples la mayoría de edad con {edad} años')
else:
    print(f'- Eres menor de edad, tienes {edad} años\n')

# Ejemplo de sentencia if elif else
print(f'-----   SENTENCIA IF ELIF ELSE   -----')
edad = 17
if edad >= 21:
    print(f'+ Cumples la mayoría de edad con {edad} años')
elif 13 <= edad < 21:
    print(f'* Eres un adolescente con {edad} años')
else:
    print(f'- Eres menor de edad, tienes {edad} años\n')