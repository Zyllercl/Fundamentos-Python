'''
    CICLOS EN PYTHON

    Def:
        - Los ciclis en Python son estructuras de control que repiten una serie de instrucciones hasta que se cumple una condición específica. Existen 2 tipos de estructuras para ejecutar ciclos, las cuales son:
            
            1.- Ciclo while:    Repite una serie de instrucciones mientras la condición a evaluar sea verdadera (True)
                Ejemplo:
                    - Sintaxis ciclo while

                        while condicion:
                            # Bloque de código a ejecutar
            
            2.- Ciclo for:      Recorre una secuencia de valores, ya sea caracteres de un string, lista, etc y ejecuta un bloque de código por cada elemento de la secuencia.
                Ejemplo:
                    - Sintaxis ciclo for

                        for variable in secuencia:
                            # Bloque de código a ejecutar

'''

'''     USO DE CICLOS    '''
# Ejemplo ciclo while
print(f'\n-----   CICLO WHILE   -----')

print(f'\n-- Imprimiendo un contador --')
# Imprimir de 1 a 5
contador = 1

while contador <= 5:
    print(f'Contador: {contador}') # Imprime Contador: {valor} hasta que se cumpla la funcion
    contador += 1

# Ejemplo ciclo for
print(f'\n-----   CICLO FOR -----')

cadena = 'Hola Mundo'
print(f'\n-- Recorriendo los caracteres de un String: "{cadena}" --')
i = 0

for letra in cadena:
    print(f'Caracter posicion {i}: {letra}') # Imprimira cada caracter del string definido
    i += 1


frutas = ['Frutilla', 'Platano', 'Guinda']
print(f'\n-- Recorriendo una lista: {frutas} --') 
x = 0

for fruta in frutas:
    print(f'Posicion {x}: {fruta}')
    x += 1