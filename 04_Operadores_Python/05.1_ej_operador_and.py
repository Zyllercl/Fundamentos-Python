'''
    SISTEMA DESCUENTOS VIP

    Def:
        - Una tienda de supermercado ofrece un descuento especial a clientes que compren 10 o más productos por día y además sean miembros de la tienda.

        - El sistema debe solicitar al cliente que indique cuántos productos ha comprado en el día y preguntarle si tiene membresía en la tienda. En caso de haber comprado 10 productos o más y es miembro de la tienda, se le realizada un descuento VIP.
'''

print(f'-----   SISTEMA DESCUENTOS VIP TIENDA VIRTUAL   -----')
# Variables
NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos has comprado hoy?: '))
membresia_vip = input('Tienes membresia VIP? (Si/No): ')

descuento = (
    cantidad_productos >= NO_PRODUCTOS_DESCUENTO
    and membresia_vip.strip().lower() == 'si'
)

print(f'\nAcceso a descuento VIP: {descuento}\n')
