'''
    MAYOR DE 2 NÚMEROS

    Def:
        - Crear un programa para indicar cual es el mayor de 2 números. El usuario debe ingresar dos numeros enteros para comparar y mandar a imprimir el número mayor
'''

print(f'-----   OBTENER EL MAYOR DE 2 NUMEROS   -----')
# Variables
numero_1 = int(input('Ingrese un número entero positivo: '))
numero_2 = int(input('Ingrese un número entero positivo: '))

if numero_1 > numero_2:
    print(f'El número mayor es: {numero_1}')
else:
    print(f'El número mayor es: {numero_2}')