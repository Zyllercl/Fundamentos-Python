# Sistemas de Numeracion 'Float' con Python Avanzado

# Numero Float
a = 3.0
print(f'a: {a:.2f}') # Expresion ":.2f" -> Dos decimales


""" # Constructor float 
        -> Puede recibir INT y STR
        -> Sobrecarga de datos: Se puede entregar distintos tipos de datos, se sobrecarga el constructor 'float' con un INT y un STRING 
"""
b = float(10) # INT
print(f'[INT] b: {b:.2f}')
b = float('10') # STR
print(f'[STR] b: {b:.2f}')

# Notacion exponencial (valores positivos o negativos)
e = 3e5 # Exponente positivo
print(f'[EXP] e: {e:.2f}')
e = 3e-5 # Exponente negativo
print(f'[EXP] e: {e:.5f}')

# Ejercicio: Realizar un calculo que involucre un 'float', el resultado sera un 'flotante'
c = 2.5 + 3
print(f'[FLOAT] c: {c:.2f}')
print(type(c))