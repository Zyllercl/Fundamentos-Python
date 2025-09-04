"""
RETO: Crear un Sistema de Inventario
====================================

Definición: 
-----------

Crear un programa de Sistema de Inventario que tenga las siguientes opciones:

    [MENU INVENTARIO]
    
    1. Mostrar Inventario
    2. Agregar Nuevo Producto
    3. Buscar Producto por ID
    4. Salir
    
    [DETALLE DEL PRODUCTO]

    ID:
    Nombre:
    Precio:
    Cantidad:
"""

print(f'[RETO] Sistema de Inventario\n')

# -------------------------------
# Definición del Inventario (Lista)
# -------------------------------
inventario = [
    # Diccionario para cada producto
    {'id': 0, 'nombre': 'Martillo', 'precio': 30000, 'cantidad': 10},
    {'id': 1, 'nombre': 'Taladro', 'precio': 120000, 'cantidad': 20}
]

# -------------------------------
# Función para Mostrar el Inventario
# -------------------------------
def mostrar_inventario():
    for producto in inventario:
        print(f'ID: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}')

# -------------------------------
# Función para Agregar Productos
# -------------------------------
def agregar_producto(): 
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

    # Método para agregar un Nuevo Producto a la Lista
    inventario.append(nuevo_producto)

    print(f'[+] Producto agregado correctamente.\n')

# -------------------------------
# Función para Buscar un Producto por ID
# -------------------------------
def buscar_producto():
    # Variables Locales
    buscar_id = int(input('\nIngrese el ID a buscar: '))

    for producto in inventario:
        if producto.get('id') == buscar_id:
            print(f'\n[~] Información del Producto:')
            print(f'ID: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}')

            return
    
    print('\n[!] Producto NO encontrado')

# -------------------------------
# Testeando la aplicación
# -------------------------------
if __name__ == '__main__':
    while True:
        print(f'''
1. Mostrar Inventario
2. Agregar Producto
3. Buscar Producto
4. Salir''')
        
        # Opción ingresada por el Usuario
        opcion = int(input('\nIngrese una opcion (1-4): '))

        # Validación de la opción ingresada por el Usuario
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            print(f'[~] Saliendo del programa...')
            break
        else:
            print('[!] Opción invalida... Seleccione una opción vlaida')
