"""
RETO: Calculadora con Funciones
===============================

Definición:
-----------

Crear un programa que realice las funciones básicas de una calculadora mostradas en un menu interactivo, las operaciones que debe contener el programa son:

    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
"""

print(f'[RETO] Calculadora Inteligente\n')

# -----------------------
# Función para Mostrar el Menu
# -----------------------
def menu():
    print(f'''
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
    ''')

    return int(input('Ingrese una opcion: '))

# -----------------------
# Función Sumar
# -----------------------
def suma(valor1, valor2):
    suma = valor1 + valor2

    print(f'La suma de {valor1} y {valor2} es: {suma:.2f}')

# -----------------------
# Función Resta
# -----------------------
def resta(valor1, valor2):
    resta = valor1 - valor2

    print(f'La resta de {valor1} y {valor2} es: {resta:.2f}')

# -----------------------
# Función Multiplicar
# -----------------------
def multiplicar(valor1, valor2):
    multi = valor1 * valor2

    print(f'La multiplicación de {valor1} y {valor2} es: {multi:.2f}')

# -----------------------
# Función Dividir
# -----------------------
def dividir(valor1, valor2):
    division = valor1 / valor2

    print(f'La división de {valor1} y {valor2} es: {division:.2f}')

# -----------------------
# Función que almacena dos valores
# -----------------------
def valores():
    valor1 = float(input('Valor 1: '))
    valor2 = float(input('Valor 2: '))

    # Retornamos una tupla
    return valor1, valor2

# -----------------------
# Función para ejecutar las operaciones matemáticas
# -----------------------
def ejecutar_operacion(opcion, salir):
    # Si la opción está entre 1 y 4 se realiza el Unpacking
    if 1 <= opcion <= 4:
        # Unpacking
        valor1, valor2 = valores()
    
    # Opciones del Menu
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

# -----------------------
# Probando la calculadora
# -----------------------
if __name__ == '__main__':
    # Variables Locales
    salir = False

    while not salir:
        # Mientras Salir sea Falso, se ejecutará las siguientes líneas de código
        opcion = menu()
        salir = ejecutar_operacion(opcion, salir)
