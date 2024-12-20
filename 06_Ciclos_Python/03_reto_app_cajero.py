'''
    APLICACION CAJERO AUTOMATICO

    Def:
        - Crear una aplicación de cajero automático. Las funciones principales de un cajero automático son las siguientes:
            - Depositar         -> Sumar dinero ingresado
            - Retirar           -> Restar dinero ingresado
            - Consultar saldo   -> Mostrar saldo actual por consola

        - El saldo puede tener un valor inicial de $100.000. 
'''

print(f'-----   BIENVENIDO A BANKANT   -----')
# Variables
saldo_inicial = 100000
salir = False

while not salir:
    print(f'''Selecciona una opción:
    1.- Consultar saldo
    2.- Depositar saldo
    3.- Retirar saldo
    4.- Salir
    ''')

    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        print(f'Tu saldo actual es: ${saldo_inicial}\n')
    elif opcion == 2:
        deposito = int(input('Ingresa el monto a depositar: '))

        if deposito <= 0:
            print('Ingrese un monto válido...\n')
        else:
            saldo_inicial += deposito
            print(f'Nuevo saldo: ${saldo_inicial}\n')
    elif opcion == 3:
        retiro = int(input('Ingrese saldo a retirar: '))

        if retiro <= saldo_inicial:
            saldo_inicial -= retiro
            print(f'Nuevo saldo: ${saldo_inicial}\n')
        else:
            print(f'Saldo insifuciente. Saldo actual ${saldo_inicial}\n')
    elif opcion == 4:
        print('Saliendo del cajero...\n')
        salir = True
    else:
        print('Opción no disponible. Selecciona una opción válida.') 
else:
    print('Finalización del programa...')  