"""
RETO: Aplicación Calculadora
============================

Definición:
-----------

Crear un programa similar a una calculadora con las siguientes opciones:

    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir
"""

print(f'[RETO] Aplicación Calculadora\n')

# Variables Locales
salir = False

# ---------------------
# Ciclo WHILE: Si 'salir' es False, el ciclo continua
# ---------------------
while not salir:
    print(f'''\n[Menu Calculadora]:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir
    ''')

    opcion = int(input('Ingrese una opción: '))

    # -------------------
    # Evaluacion de la opción seleccionada por el usuario
    # -------------------

    # Opcion 1: SUMA
    if opcion == 1:
        numero_1 = int(input('Ingrese el numero 1: '))
        numero_2 = int(input('Ingrese el numero 2: '))

        suma = numero_1 + numero_2

        print(f'\nLa suma de ({numero_1} + {numero_2}) es: {suma}\n')
    # Opcion 2: RESTA
    elif opcion == 2:
        numero_1 = int(input('Ingrese el numero 1: '))
        numero_2 = int(input('Ingrese el numero 2: '))

        resta = numero_1 - numero_2

        print(f'\nLa resta de ({numero_1} - {numero_2}) es: {resta}\n')
    # Opcion 3: MULTIPLICACION
    elif opcion == 3:
        numero_1 = int(input('Ingrese el numero 1: '))
        numero_2 = int(input('Ingrese el numero 2: '))

        multiplicacion = numero_1 * numero_2
        
        print(f'\nLa multiplicación de ({numero_1} * {numero_2}) es: {multiplicacion}\n')
    # Opcion 4: DIVISION
    elif opcion == 4:
        numero_1 = int(input('Ingrese el numero 1: '))
        numero_2 = int(input('Ingrese el numero 2: '))

        if numero_1 == 0 or numero_2 == 0:
            print('[ERROR] No se puede divisir un número en 0')
        else:
            division = numero_1 / numero_2
            print(f'\nLa division de ({numero_1} / {numero_2}) es: {division}\n')
    # Opcion 5: SALIR
    elif opcion == 5:
        print('Cerrando calculadora...\n')
        salir = True
    else:
        print('Opción no disponible. Selecciona una opción válida.') 
else:
    print('Finalización del programa...')  