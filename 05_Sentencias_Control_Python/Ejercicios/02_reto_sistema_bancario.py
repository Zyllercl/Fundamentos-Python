'''
    SISTEMA BANCARIO

    Def:
        - Imaginar que nos encontramos dentro de un sistema bancario, se debe crear un programa que solicite al usuario si desea continuar dentro del sistema. Para ello, se debe utilizar el operador 'not' para aplicar la lógica inversa, considerar lo siguiente:
            1.- Si NO deseamos salir del sistema, imprimir: 'Continuamos dentro del sistema...'
            2.- De lo contrario, imprimir: 'Saliendo del sistema...'
'''

print(f'-----   SISTEMA BANCARIO   -----')
# Variables
salida_sistema = input('Deseas salir del sistema? (Si/No): ')
salir_del_sistema = salida_sistema.strip().lower() == 'si'

# Si NO deseas salir del sistema, es decir, salir_de_sistema = False
if not salir_del_sistema:
    print('Continuamos dentro del sistema...')
else:
    print('[!] Saliendo del sistema...')