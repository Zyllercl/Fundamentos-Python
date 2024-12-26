'''
    COMPRENSION DE LISTAS (List Comprehension)

    Def:
        - Las 'List Comprehension' es una forma concisa y eficiente de crear listas a partir de otros iterables (listas, tuplas, set o diccionarios).
        - Permite filtrar elementos y aplicar expresiones a cada elemento de un interable, es decir, se puede crear una iteracion dentro de una lista para simplificar la declaraciones de nuevos valores permitiendo que el código sea más regible.

            Ejemeplo:
                - Sintaxis Comprension de Listas
                    list_comprehension = [nueva_expresion for elemento in iterable if condicion]

                    donde:
                        - 'nueva_expresion':    Es la expresión que define cómo se modifica o procesa cada elemento del iterable
                        - 'elemento':           Variable que representa a cada elemento del iterable original
                        - 'iterable':           Secuencaia o colección sobre la cual se va a iterar
                        - 'condicion:           (Opcional) Es una condición para filtrar los elementos del iterable      
'''

print(f'-----   LIST COMPREHENSION (Comprensión de Listas)   -----')
# Ejemplo 1: Lista sólo los numeros pares de una lista
numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
print(f'Numeros pares: {pares}')

# Ejemplo 2: Lista el valor al cuadrado de cada numero
cuadrado = [x**2 for x in numeros]
print(f'Numeros: {cuadrado}\n')

# Ejemplo 3: Listar un saludo a varios nombres de una lista
nombres = ['Clarke', 'Daenaryes', 'Jon']

saludar = [f'Hola {nombre}' for nombre in nombres]
print(saludar)