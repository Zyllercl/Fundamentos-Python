"""
RETO: Identificar la estación del año
=====================================

Definición:
-----------

Crear un programa para identificar en qué estación del año nos encontramos. Para ello, se debe solicitar al usuario ingresar el mes actual (valor numérico de 1 al 12). Considerar lo siguiente:
    1. Verano                  -> Meses 1, 2, 3 y 12
    2. Otoño                   -> Meses 4, 5, 6
    3. Invierno                -> Meses 7, 8
    4. Primavera               -> Meses 9, 10, 11
    5. Estación Desconocida    -> Mes no existente
"""

print(f'[IDENTIFICAR ESTACIÓN DEL AÑO]\n')
# -----------------------------
# Solicitar el mes actual al usuario
# -----------------------------
mes = int(input('Ingrese el número del mes actual: '))
estacion = None

# -----------------------------
# Identificar la estación del año según el mes ingresado
# -----------------------------
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