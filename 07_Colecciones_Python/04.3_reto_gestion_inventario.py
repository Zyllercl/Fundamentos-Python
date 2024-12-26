'''
    GESTION DE INVENTARIO

    Def: 
        - Crear un programa para gestionar el inventairo de un almacen. Se debe utilizar una lista de Python para mantener un registro de los productos disponibles en el almacen. Para almacenar el detalle del producto se debe utilizar un duccionario, con el id, nombre, precio y cantidad disponible del producto en almacen.
'''

print(f'-----   GESTION DE INVENTARIO   -----')
# Variables
inventario = []

cantidad_productos = int(input('¿Cuantos productos vas a ingresar?: '))

for indice in range(cantidad_productos):
    print(f'[+] Proporciona los valores del producto {indice + 1}')
    # Variables producto
    nombre = input('Nombre: ')
    precio = int(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    
    # Creación del diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

    # Agregar el nuevo producto al inventario (tipo diccionario)
    inventario.append(producto)

# Inventairo Inicial
print(f'\nDetalle Inventario: {inventario}')

# Buscar un producto por id
buscar_id = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None

for producto in inventario:
    if producto.get('id') == buscar_id:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(f'\n--- Información del producto ---')
    print(f'''ID: {producto_encontrado.get('id')}
Nombre: {producto_encontrado.get('nombre')}
Precio: {producto_encontrado.get('precio')}
Cantidad: {producto_encontrado.get('cantidad')}
    ''')
else:
    print(f'[!] Producto con ID {buscar_id} NO encontrado!')


# Mostrar el Inventario de forma detallada
print(f'\n--- Inventario Detallado ---')

for producto in inventario:
    print(f'''ID: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: {producto.get('precio')}
    Cantidad: {producto.get('cantidad')}
    ''')

