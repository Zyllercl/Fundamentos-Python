'''
    PROMEDIO DE CALIFICACIONES

    Def: 
        - Crear un programa para realizar el cálculo promedio de calificaciones.

        - Solicitar al usuario el número de calificaciones a utilizar para obtener el promedio, luego solicitar cada calificación al usuario. Finalmente realizar el calculo del promedio de las notas ingresadas.
'''

print(f'-----   PROMEDIO DE CALIFICACIONES   -----')
# Variables
notas = []
cantidad_notas = int(input('Ingrese la cantidad de notas: '))

# Iteracion de cada elemento de la lista para agregar un nuevo elemento
for indice in range(cantidad_notas):
    nota_ingresada = float(input(f'Nota[{indice}]: '))
    notas.append(nota_ingresada) # Agregando notas a la lista

print(f'\nLas notas ingresadan son: {notas}\n')

suma_notas = sum(notas) # Suma lista de notas
promedio = float(suma_notas / cantidad_notas)

print(f'El promedio es: {promedio:.2f}')