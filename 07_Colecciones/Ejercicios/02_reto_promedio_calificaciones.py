"""
RETO: Promedio de calificaciones
================================

Definición:
-----------

Crear un programa para realizar el cálculo promedio de calificaciones.

Consideraciones:

    - Solicitar al usuario el número de calificaciones a utilizar para obtener el promedio, luego solicitar cada calificación al usuario. Finalmente realizar el calculo del promedio de las notas ingresadas.

"""

print(f'[RETO] Promedio de calificaciones\n')

# --------------------
# Variables
# --------------------
notas = [] # Lista vacia
cantidad_notas = int(input('Ingrese la cantidad de notas: '))

# --------------------
# Iteracion de cada elemento de la lista para agregar un nuevo elemento
# --------------------
for indice in range(cantidad_notas):
    # Solicitar nota al usuario
    nota_ingresada = float(input(f'Nota[{indice}]: '))
    # Agregar nota a la lista
    notas.append(nota_ingresada) 

print(f'\nLas notas ingresadan son: {notas}\n')

# --------------------
# Calculo del promedio
# --------------------
suma_notas = sum(notas)
promedio = float(suma_notas / cantidad_notas)

print(f'El promedio es: {promedio:.2f}')