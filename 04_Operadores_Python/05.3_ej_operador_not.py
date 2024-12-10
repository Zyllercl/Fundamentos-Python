'''
    GENERACION TICKET VENTA

    Def:
        - El sistema necesita el precio de cada producto adquirido en donde el usuario deberá ingresarlos manualmente. Posteriormente se debera imprimir por consola la suma de cada producto junto con el impuesto.
'''

print(f'-----   GENERACION TICKET    -----')
# Variables
IMPUESTO = 0.19
precio_pan = float(input('Precio Pan: '))
precio_tomate = float(input('Precio Tomate: '))
precio_hamburgesa = float(input('Precio Hamburgesa: '))
precio_lechuga = float(input('Precio Lechuga: '))
descuento_porcentaje = int(input('Aplicar descuento (%)?: '))

precio_neto_total = precio_pan + precio_tomate + precio_hamburgesa + precio_lechuga
descuento = precio_neto_total * (descuento_porcentaje / 100)
precio_neto_descuento = precio_neto_total - descuento
impuestos = precio_neto_descuento * 0.19
precio_total = precio_neto_descuento + impuestos

print(f'''\n
Productos: Pan - Tomate - Lechuga - Hamburguesa
Precio Neto: {precio_neto_total:.2f}
Descuento: {descuento} ({descuento_porcentaje}%)
Precio Descuento: {precio_neto_descuento}
Impuestos (19%): {impuestos:.2f}
Precio Total: {precio_total:.2f}\n
''')


