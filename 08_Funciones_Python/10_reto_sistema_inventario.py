'''
    SISTEMA DE INTENVARIO

    Def:
        - Crear un programa de sistema de inventario que tenga las siguientes opciones:
        
            Mostrar un menú:
                1. Mostrar inventario
                2. Agregar nuevo producto
                3. Buscar producto por ID
                4. Salir
            
            Detalle del producto:
                ID      Precio      Nombre      Cantidad
'''

print(f'-----   SISTEMA DE INVENTARIO   -----')

# Inventario del almacen
inventario = [
    {'id': 0, 'nombre': 'Tornillos', 'precio': 300, 'cantidad': 200},
    {'id': 1, 'nombre': 'Taladro', 'precio': 87990, 'cantidad': 50}
]

# Funcion mostrar inventario
def mostrar_inventario():
    print(f'\n[-----   INVENTARIO BODEGA   -----]')

    for producto in inventario:
        print(f'ID: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}')

# Funcion agregar producto
def agregar_producto():
    print(f'\n[-----   AGREGAR PRODUCTO   -----]')
    
    # Variables locales
    id = int(input('ID: '))
    nombre = input('Nombre: ')
    precio = int(input('Precio: '))
    cantidad = int(input('Cantidad: '))

    nuevo_producto = {
        'id': id,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

    inventario.append(nuevo_producto)
    print(f'\n[+] Producto agregado correctamente.')

# Funcion buscar producto
def buscar_producto():
    print(f'\n[-----   BUSCAR PRODUCTO   -----]')

    buscar_id = int(input('Ingrese el ID a buscar: '))
    for producto in inventario:
        if producto.get('id') == buscar_id:
            print(f'[~] Información del Producto: \n')
            print(f'ID: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}')

            return
    
    print('\n[!] Producto NO encontrado')

if __name__ == '__main__':
    while True:
        print(f'''
    1. Mostrar Inventario
    2. Agregar Producto
    3. Buscar Producto
    4. Salir''')
        
        opcion = int(input('\nIngrese una opcion (1-4): '))

        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            print(f'Saliendo del programa...')
            break
        else:
            print('[!] Opción invalida... Seleccione una opción vlaida')
