'''
    MAQUINA DE SNACKS

    Def:
        1. Crear un programa donde se podrá comprar snacks de una lista inicial. 
        2. Cada snack debe tener: id, nombre, precio
        3. Para comprar un snack se debe indicar el ID del snack a comprar y se debe agregar a una lista de productos comprados
        4. Además, se debe mostrar una boleta de venta con el total de productos y el total de la venta             
'''

print(f'-----   MAQUINA DE SNACKS  -----')

# Variables Globales
productos_maquina = [
    {'id': 1, 'nombre': 'Monster', 'precio': 2000},
    {'id': 2, 'nombre': 'Mantecol', 'precio': 750},
    {'id': 3, 'nombre': 'Coca-Cola', 'precio': 1000},
    {'id': 4, 'nombre': 'Takis', 'precio': 2500},
]

productos_comprados = []

# Funcion mostrar snacks
def mostrar_snacks():
    print(f'\n[-----   MAQUINA SNACKS   -----]')

    for producto in productos_maquina:
        print(f'ID: {producto.get("id")} -> {producto.get("nombre")} - $ {producto.get("precio")}')

# Funcion comprar snacks
def comprar_snacks():
    id_producto = int(input('Ingresa el ID del snack: '))
    producto_encontrado = buscar_producto_maquina(id_producto)

    if producto_encontrado is not None:
        productos_comprados.append(producto_encontrado)
        print(f'Producto aregado: {producto_encontrado}')
    else:
        print(f'[!] Producto NO encontrado con el ID: {id_producto}')


# Funcion mostrar boleta
def mostrar_boleta():
    boleta = f'\n[-----   BOLETA ELECTRONICA   -----]'
    total = 0

    for producto in productos_comprados:
        boleta += f'\n- {producto.get("nombre")} - ${producto.get("precio")}'
        total += producto.get('precio')
    boleta += f'\nTOTAL -> ${total}'

    print(boleta)


# Funcion buscar producto en la maquina
def buscar_producto_maquina(id_ingresado):
    for producto in productos_maquina:
        if producto.get('id') == id_ingresado:
            return producto
    # Si no encontro el producto en la maquina devolver None
    return None
        

if __name__ == '__main__':
    while True:
        print(f'''\nMENU:
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar Boleta
        4. Salir''')
        
        opcion = int(input('\nIngrese una opcion: '))
        
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostrar_boleta()
        elif opcion == 4:
            print(f'Saliendo del programa...')
            break
        else:
            print(f'[!] Error, seleccione una opcion valida...')