'''
    IDENFITICAR LA ESTACIÓN DEL AÑO

    Def:
        - Crear un programa para identificar en que estación del año nos encontramos, para ello se debe solicitar al usuario ingresar el mes actual (valor númerico de 1 al 12). Considerar lo siguiente:
            1.- Verano                  -> Meses 1, 2, 3 y 12
            2.- Otoño                   -> Meses 4, 5, 6
            3.- Invierno                -> Meses 7, 8
            4.- Privamera               -> Meses 9, 10, 11
            5.- Estación Desconocida    -> Mes no existente
'''

print(f'-----   IDENFITICAR LA ESTACIÓN DEL AÑO   -----')
# Variables
mes = int(input('Ingrese el número del mes actual: '))
estacion = None

if mes == 1 or mes == 2 or mes == 3 or mes == 12:
    estacion = 'Verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Otoño'
elif mes == 7 or mes == 8:
    estacion = 'Invierno'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Primavera'
else:
    estacion = 'Estación desconocida'

print(f'El mes ({mes}) ingresado corresponde a: {estacion}')