'''
    MENU ITERATIVO

    Def: Realizar un menú iterativo que permita al usuario seleccionar 3 opciones, las cuales son: 
        1.- Crear cuenta
        2.- Eliminar cuenta
        3.- Salir

        - Al seleccionar una opcion, se le mostrará por consola al usuario su selección. Si el usuario elige la opción 3, el programa terminará.
'''

# Variables
salir = False

while not salir:
    print(f'''MENU ITERATIVO:
    1.- Crear cuenta
    2.- Eliminar cuenta
    3.- Salir''')

    opcion = int(input('Ingrese una opcion: '))

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