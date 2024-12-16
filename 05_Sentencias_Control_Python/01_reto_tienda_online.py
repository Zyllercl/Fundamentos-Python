'''
    TIENDA ONLINE 

    Def:
        - Crear un programa que ofrezca descuentos dependiendo del monto ingresado.

        Considerar los siguientes punto:
            1.- Si el valor es más de $15.000 y tiene membresia en la tienda (Descuento de 10%)
            2.- Si sólo tiene membresia en la tienda (Descuento de 5%)
            3.- Si no es miembro y compro menos de $15.000 (Descuento de 0%)
'''

print(f'-----   SISTEMA DE DESCUENTO TIENDA ONLINE   -----')

DESCUENTO_SOLO_VIP = 0.05
DESCUENTO_VIP_MONTO = 0.10
MONTO_MINIMO = 15000

monto = int(input('Cual es el monto comprado?: '))
membresia = input('Tienes membresia VIP? (Si/No): ').strip().lower()

if monto >= MONTO_MINIMO and membresia == "si":
    print(f'\nAplicando descuendo del {DESCUENTO_VIP_MONTO * 100:.0f}% \n')
    monto_total_desc = monto - (monto * DESCUENTO_VIP_MONTO)
    print(f'Monto ingresado: {monto}')
    print(f'Monto descontado: {monto * DESCUENTO_VIP_MONTO}')
    print(f'Monto Total: {monto_total_desc}')
elif membresia == "si":
    print(f'\nAplicando descuendo del {DESCUENTO_SOLO_VIP * 100:.0f}% \n')
    monto_total_desc = monto - (monto * DESCUENTO_SOLO_VIP)
    print(f'Monto ingresado: {monto}')
    print(f'Monto descontado: {monto * DESCUENTO_SOLO_VIP}')
    print(f'Monto Total: {monto_total_desc}')
else:
    print(f'\nNo posees descuentos...')
    print(f'Monto Total: {monto}')