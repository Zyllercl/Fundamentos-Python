'''
    CALCULADORA CON FUNCIONES

    Def:
        - Crear un programa para agregar las operaciones básicas de una calculadora:

            Las operacionbes que debe tener son:
                1. Sumar
                2. Restar
                3. Multiplicar
                4. Dividir
                5. Salir

            Además, se debe crear un menú para mostrar cada opcion.       
'''

print(f'-----   CALCULADORA CON FUNCIONES   -----')

# Funcion Menu
def menu():
    print(f'''\nMENU CALCULADORA:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
    ''')

    return int(input('Ingrese una opcion: '))

# Funciones Operaciones Matemáticas
def suma(valor1, valor2):
    suma = valor1 + valor2
    print(f'La suma de {valor1} y {valor2} es: {suma:.2f}')

def resta(valor1, valor2):
    resta = valor1 - valor2
    print(f'La resta de {valor1} y {valor2} es: {resta:.2f}')

def multiplicar(valor1, valor2):
    multi = valor1 * valor2
    print(f'La resta de {valor1} y {valor2} es: {multi:.2f}')

def dividir(valor1, valor2):
    division = valor1 / valor2
    print(f'La resta de {valor1} y {valor2} es: {division:.2f}')

def valores():
    valor1 = float(input('Valor 1: '))
    valor2 = float(input('Valor 2: '))

    # Retornamos una tupla
    return valor1, valor2

def ejecutar_operacion(opcion, salir):
    # Valores de las opciones del menu
    if 1 <= opcion <= 4:
        # Unpacking
        valor1, valor2 = valores()
    
    if opcion == 1:
        suma(valor1, valor2)
    elif opcion == 2:
        resta(valor1, valor2)
    elif opcion == 3:
        multiplicar(valor1, valor2)
    elif opcion == 4:
        dividir(valor1, valor2)
    elif opcion == 5:
        print('[~] Saliendo del programa...')
        salir = True
    else:
        print(f'[!] Opcion no valida...')
    return salir

if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = menu()
        salir = ejecutar_operacion(opcion, salir)
