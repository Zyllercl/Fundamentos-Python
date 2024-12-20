'''
    DIBUJANDO UN ARBOL DE NAVIDAD
'''

print(f'-----   DIBUJANDO UN ARBOL DE NAVIDAD   -----')
# Variables
numero_filas = int(input('Ingrese la cantidad de filas: '))

for fila in range(1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila) #  Calculo de espacio en blanco por cada fila
    asteriscos = '*' * (2 * fila -1) # Calculo de asteriscos a rellenar por cada fila

    print(f'{espacios_blanco}{asteriscos}')