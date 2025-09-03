""""
RETO: Dibujar un árbol de Navidad
=================================

Definición:
-----------

Crear un programa que dibuje un árbol de Navidad utilizando asteriscos (*). El programa debe solicitar al usuario la cantidad de filas que tendrá el árbol y luego imprimir el árbol en la consola. Cada fila del árbol debe tener un número impar de asteriscos, centrados para formar la forma del árbol.
"""

print(f'[RETO] Dibujar un árbol de Navidad\n')

# Ingreso de datos: Número de filas
numero_filas = int(input('Ingrese la cantidad de filas: '))

# Recorrido de filas para dibujar el árbol
for fila in range(1, numero_filas + 1):
    # Cálculo de espacios en blanco y asteriscos
    espacios_blanco = ' ' * (numero_filas - fila)
    # Cálculo de asteriscos (número impar) 
    asteriscos = '*' * (2 * fila -1)

    print(f'{espacios_blanco}{asteriscos}')