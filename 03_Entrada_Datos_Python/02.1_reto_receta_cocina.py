'''     CREAR UN ṔROGRAMA DE RECETA DE COCINA    '''

'''
    INSTRUCCIONES: Crear un programa para solicitar datos para una receta de cocina. Los valores que debe introducir son los sigiuientes:
        - Nombre de la Receta
        - Ingredientes
        - Tiempo de preparación (en minutos)
        - Dificultad (Fácil, Media, Dificil)
'''

print('++++\tCREA TU RECETA\t++++')

# Variables
nombre_receta = input('Nombre de la receta: ')
ingredientes_receta = input('Ingrese los ingredientes: ')
tiempo_preparacion = int(input('Tiempo de preparacion (min): '))
dificultad_receta = input('Dificultad receta (Facil, Media, Dificil): ')

print('\n---------------\n')
print(f'Nombre Receta: {nombre_receta}')
print(f'Ingedientes: {ingredientes_receta}')
print(f'Tiempo de Preparación: {tiempo_preparacion}')
print(f'Dificultad: {dificultad_receta}')