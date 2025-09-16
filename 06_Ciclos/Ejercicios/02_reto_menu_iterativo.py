"""
RETO: Menu iterativo
====================

Definición:
-----------

Realizar un menú iterativo que permita al usuario seleccionar 3 opciones, las cuales son:

    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir

Al seleccionar una opcion, se le mostrará por consola al usuario su selección. Si el usuario elige la opción 3 (salir), el programa terminará.
"""

# Variables Locales
salir = False

# ---------------------
# Ciclo WHILE: Si 'salir' es False, el ciclo continua
# ---------------------
while not salir:
    print(f'''\n[Menu Iterativo]:
    1.- Crear cuenta
    2.- Eliminar cuenta
    3.- Salir''')

    opcion = int(input('\nIngrese una opcion: '))

    # Evaluar la opción seleccionada por el usuario
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando ccuenta...\n')
    elif opcion == 3:
        print('Saliendo del programa...\n')
        salir = True
    else:
        print('Opción invalida. Selecciona otra opción....\n')
else:
    print('Finalización del programa!\n')