"""
Uso de Ciclos en Python
=======================
Este script demuestra el uso de ciclos 'while' y 'for' en Python.
"""

# ---------------------
# Ciclo While en Python
# ---------------------
print(f'[CICLO WHILE]\n')

print(f'[+] Imprimiendo numeros del 1 al 5 usando while')
# Imprimir de 1 a 5
contador = 1

while contador <= 5:
    print(f'Contador: {contador}') # Imprime Contador: {valor} hasta que se cumpla la funcion
    contador += 1

# ---------------------
# Ciclo For en Python
# ---------------------
print(f'[CICLO FOR]\n')

cadena = 'Hola Mundo'
print(f'[+] Recorriendo los caracteres de un String: "{cadena}"')

# Índice posición 0
i = 0

# Recorriendo cada caracter en la cadena
for letra in cadena:
    # Imprime la posicion y el caracter en esa posicion
    print(f'Caracter posicion {i}: {letra}')
    # Incremento del índice
    i += 1

# ---------------------
# Ejemplo recorrer una lista
# ---------------------
frutas = ['Frutilla', 'Platano', 'Guinda']
print(f'\n[+] Recorriendo una lista de frutas')

# Índice posición 0
x = 0

# Recorriendo cada fruta en la lista
for fruta in frutas:
    print(f'Posicion {x}: {fruta}')
    x += 1