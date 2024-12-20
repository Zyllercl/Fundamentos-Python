'''
    APLICACION CALCULADORA

    Def:
        - Crear un programa similar a una calculadora con las siguientes opciones:
            1.- Suma
            2.- Resta
            3.- Multiplicación
            4.- División
            5.- Salir
'''

print(f'-----   CALCULADORA INTELIGENTE   -----')
# Variables
salir = False

while not salir:
    print(f'''Selecciona una opción:
    1.- Suma
    2.- Resta
    3.- Multiplicación
    4.- División
    5.- Salir
    ''')

    opcion = int(input('Ingrese una opción: '))

    # Suma
    if opcion == 1:
        numero_1 = int(input('Ingrese el numero 1: '))
        numero_2 = int(input('Ingrese el numero 2: '))

        suma = numero_1 + numero_2

        print(f'\nLa suma de ({numero_1} + {numero_2}) es: {suma}\n')
    # Resta
    elif opcion == 2:
        numero_1 = int(input('Ingrese el numero 1: '))
        numero_2 = int(input('Ingrese el numero 2: '))

        resta = numero_1 - numero_2

        print(f'\nLa resta de ({numero_1} - {numero_2}) es: {resta}\n')
    # Multiplicacion
    elif opcion == 3:
        numero_1 = int(input('Ingrese el numero 1: '))
        numero_2 = int(input('Ingrese el numero 2: '))

        multiplicacion = numero_1 * numero_2
        
        print(f'\nLa multiplicación de ({numero_1} * {numero_2}) es: {multiplicacion}\n')
    # Division
    elif opcion == 4:
        numero_1 = int(input('Ingrese el numero 1: '))
        numero_2 = int(input('Ingrese el numero 2: '))

        if numero_1 == 0 or numero_2 == 0:
            print('[ERROR] No se puede divisir un número en 0')
        else:
            division = numero_1 / numero_2
            print(f'\nLa division de ({numero_1} / {numero_2}) es: {division}\n')
    # Salir
    elif opcion == 5:
        print('Cerrando calculadora...\n')
        salir = True
    else:
        print('Opción no disponible. Selecciona una opción válida.') 
else:
    print('Finalización del programa...')  