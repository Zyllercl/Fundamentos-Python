"""
Sistema descuentos VIP
========================

Definición:
-----------

Una tienda de supermercado ofrece un descuento especial a clientes que compren 10 o más productos por día y además sean miembros de la tienda.
El sistema debe solicitar al cliente que indique cuántos productos ha comprado en el día y preguntarle si tiene membresía en la tienda. En caso de haber comprado 10 productos o más y es miembro de la tienda, se le realizará un descuento VIP.
"""


# ---------------------------
# Ejemplo de uso del operador AND
# ---------------------------
print(f'[SISTEMA DESCUENTOS VIP]\n')


# ---------------------------
# Entrada de datos
# ---------------------------
NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos has comprado hoy?: '))
membresia_vip = input('Tienes membresia VIP? (Si/No): ')

descuento = (
    cantidad_productos >= NO_PRODUCTOS_DESCUENTO
    and membresia_vip.strip().lower() == 'si'
)

print(f'\nAcceso a descuento VIP: {descuento}\n')
