"""
RETO: Aplicación Cajero Automático
==================================

Definición:
-----------

Crear una aplicación de cajero automático que permita al usuario realizar las siguientes operaciones:

    1. Depositar dinero     -> Sumar dinero ingresado
    2. Retirar dinero       -> Restar dinero ingresado
    3. Consultar saldo      -> Mostrar saldo actual por consola
    4. Salir
"""

print(f'[RETO] Aplicación Cajero Automático\n')

# Variables Locales
saldo_inicial = 100000
salir = False

# ---------------------
# Ciclo WHILE: Si 'salir' es False, el ciclo continua
# ---------------------
while not salir:
    print(f'''[Menu Cajero Automático]:
    1.- Consultar saldo
    2.- Depositar saldo
    3.- Retirar saldo
    4.- Salir
    ''')

    opcion = int(input('Ingrese una opción: '))

    # Evaluar la opción seleccionada por el usuario
    if opcion == 1:
        # Imprime el saldo actual por consola
        print(f'\nTu saldo actual es: ${saldo_inicial}\n')
    elif opcion == 2:
        deposito = int(input('Ingresa el monto a depositar: '))

        # Valida que el monto a depositar sea mayor a 0
        if deposito <= 0:
            print('Ingrese un monto válido...\n')
        else:
            # Suma el monto depositado al saldo inicial
            saldo_inicial += deposito
            print(f'\nNuevo saldo: ${saldo_inicial}\n')
    elif opcion == 3:
        retiro = int(input('Ingrese saldo a retirar: '))

        # Valida que el monto a retirar sea mayor a 0
        if retiro <= saldo_inicial:
            # Resta el monto retirado al saldo inicial
            saldo_inicial -= retiro
            print(f'\nNuevo saldo: ${saldo_inicial}\n')
        else:
            # Muestra mensaje de saldo insuficiente
            print(f'\nSaldo insifuciente. Saldo actual ${saldo_inicial}\n')
    elif opcion == 4:
        print('Saliendo del cajero...\n')
        salir = True
    else:
        print('Opción no disponible. Selecciona una opción válida.') 
else:
    print('Finalización del programa...')  