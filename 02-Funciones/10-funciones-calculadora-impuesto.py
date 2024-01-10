
# Calculadora de Impuestos
def pago_impuesto(monto, iva):
    pago_total = monto + (monto * (iva/100))
    return pago_total

monto = float(input('Monto sin impuesto: '))
iva = float(input('Monto impuesto (%): '))

monto_total = pago_impuesto(monto, iva)
print(f'Pago total con impuestos: {monto_total}')