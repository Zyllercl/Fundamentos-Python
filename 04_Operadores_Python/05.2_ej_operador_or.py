'''
    SISTEMA DE PRESTAMO

    Def:
        - Crear un sistema para una biblioteca, la cual presta libros si cumple con cualquiera de las siguientes condiciones:
            1.- El usuario tiene credencial de estudiante
            2.- El usuario vive a no más de 3Km a la redonda
            
            Si cumple con cualquiera de estas condiciones, se le puede prestar el libro.
'''

print(f'-----   SISTEMA DE PRESTAMOS   -----')
# Variables
DISTANCIA_REDONDA = 3
es_estudiante = input('Tienes credencial estudiantil? (Si/No): ')
distancia = int(input('A cuantos Km vives de la biblioteca?: '))

resultado = (distancia <= DISTANCIA_REDONDA) or (es_estudiante.strip().lower() == 'si')

print(f'¿Puedo tomar prestado un libro?: {resultado}')