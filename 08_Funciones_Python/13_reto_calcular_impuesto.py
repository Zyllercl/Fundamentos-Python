'''
    CALCULAR IMPUESTOS

    Def:
        - Crear una funcion que permita calcular un pago incluyendo el impuesto

            Formula:
                pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)    
'''

print(f'-----   CALCULAR IMPUESTOS   -----')

# Funcion calcular impuesto
def calcular_impuesto(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    
    return pago_total
    
pago_sin_impuesto = int(input('Ingrese el pago sin impuesto: '))
impuesto = int(input('Ingrese el impuesto (sin %): '))

pago_con_impuesto = calcular_impuesto(pago_sin_impuesto, impuesto)

print(f'Pago con impuesto: {pago_con_impuesto}')
