"""
RETO: Gestión de Inventario
===========================

Definición:
-----------

Crear un programa para gestionar el inventario de un almacen. Considerar lo siguiente:

    1. Crear una Lista para mantener los registros de los productos disponibles en el almacen.
    2. Crear un diccionario para almacenar el detalle del producto, los cuale son:
        - ID
        - Nombre
        - Precio
        - Cantidad Disponible
"""

print(f'[RETO] Gestión de Inventario')

# ----------------------
# Creacicón de la Lista de productos
# ----------------------

# Lista Vacia
inventario = []

# Solicitud al usuario la cantidad de productos a agregar
cantidad_productos = int(input('¿Cuantos productos vas a ingresar?: '))

# Recorre la cantidad de productos ingresado por el usuario
for indice in range(cantidad_productos):
    # Ingreso del detalle del producto
    print(f'[+] Proporciona los detalles del producto {indice + 1}')
    
    # Variables producto
    nombre = input('Nombre: ')
    precio = int(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    
    # Creación del diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

    # Agregar el nuevo producto (tipo diccionario) al inventario
    inventario.append(producto)

# ----------------------
# Inventairo Inicial
# ----------------------
print(f'\n[INVENTARIO INICIAL] \n\n{inventario}')

# ----------------------
# Buscar un producto por ID
# ----------------------
buscar_id = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None

# Iteración del ID del producto en 'inventario'
for producto in inventario:
    if producto.get('id') == buscar_id:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(f'\n[INFO] Producto con ID {buscar_id}')
    print(f'''ID: {producto_encontrado.get('id')}
Nombre: {producto_encontrado.get('nombre')}
Precio: {producto_encontrado.get('precio')}
Cantidad: {producto_encontrado.get('cantidad')}
    ''')
else:
    print(f'\n[!] Producto con ID {buscar_id} NO encontrado!')

# ----------------------
# Mostrar el Inventario de forma detallada
# ----------------------
print(f'\n[INVENTARIO DETALLADO]')

for producto in inventario:
    print(f'''ID: {producto.get('id')}
        Nombre: {producto.get('nombre')}
        Precio: {producto.get('precio')}
        Cantidad: {producto.get('cantidad')}
    ''')

