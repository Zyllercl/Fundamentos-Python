"""
RETO: Reserva de Hotel
======================

Definición:
-----------

Crear un programa de reservación de un hotel. Se debe pedir al usuario la siguiente información:
    1. Nombre
    2. Cuantos días de estadía estará en el hotel
    3. Dormitorio con vista al mar

El hotel tiene las siguientes tarifas:
    - Dormitorio sin vista al mar: $ 150.500 x día
    - Dormitorio con vista al mar: $ 190.500 x día

El programa debe calcular el costo total de la estadía dependiendo si escogió un dormitorio con vista al mar o no.
"""

print(f'[RETO RESERVA HOTEL]\n')

# -----------------------------
# Definición de constantes
# -----------------------------
DORMITORIO_SIN_VISTA_MAR = 15050
DORMITORIO_CON_VISTA_MAR = 19050

# -----------------------------
# Solicitar datos al usuario
# -----------------------------
nombre_cliente = input('Ingrese su nombre: ')
cantidad_dias = int(input('¿Cuantos días estará en el hotel?: '))
tipo_dormitorio = input('¿Dormitorio con vista al mar? (Si/No): ')

tipo_dormitorio = tipo_dormitorio.strip().lower() == 'si' # Si es verdadero, devolvera True

# -----------------------------
# Calcular costo total de la estadía
# -----------------------------
if tipo_dormitorio:
    costo_total = cantidad_dias * DORMITORIO_CON_VISTA_MAR
else:
    costo_total = cantidad_dias * DORMITORIO_SIN_VISTA_MAR

print(f'''\n-----DETALLE DE RESERVA-----
Cliente: {nombre_cliente}
Días de estadía: {cantidad_dias}
Dormitorio con vista al mar: {'SI' if tipo_dormitorio else "NO"}
Costo total: $ {costo_total:.2f} CLP
''')