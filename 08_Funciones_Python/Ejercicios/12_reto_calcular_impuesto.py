"""
RETO: Calcular Impuestos 
========================

Definición:
-----------

Crear una función que permita calcular un pago incluyendo IVA.

[FORMULA] pago_total = pago_sin_impuesto + pago_sin_impuesto * ( impuesto / 100 )
"""

print(f'[RETO] Calcular Impuestos (IVA)\n')

# ----------------------------
# Función Calcular Impuestos
# ----------------------------
def calcular_impuesto(pago_sin_impuesto, impuesto):
    # Formula para precio + IVA
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    
    return pago_total

# ----------------------------
# Variables Globales
# ----------------------------    
pago_sin_impuesto = int(input('Ingrese el pago sin impuesto: '))

impuesto = int(input('Ingrese el impuesto (sin %): '))

pago_con_impuesto = calcular_impuesto(pago_sin_impuesto, impuesto)

print(f'Total (+IVA): {pago_con_impuesto}')
 