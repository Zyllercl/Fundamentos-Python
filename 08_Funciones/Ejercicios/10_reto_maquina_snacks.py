"""
RETO: Máquina de Snacks
=======================

Definición:
-----------

1. Crear un programa donde se podrá comprar snacks de una Lista Inicial.
2. Cada Snack debe tener la siguiente información:
    - ID
    - Nombre
    - Precio
3. Para comprar un Snack debe ingresar el ID del Snack y se debe agregar a una Lista de Productos Comprados.
4. Una vez finalice la compra, se debe mostrar una Boleta de venta con el Total de Productos y el Total de la Venta.
"""

print(f'[RETO] Máquina de Snacks\n')

# ------------------------
# Variables Globales
# ------------------------

# Lista de productos de la máquina de snacks
productos_maquina = [
    {'id': 1, 'nombre': 'Monster', 'precio': 2000},
    {'id': 2, 'nombre': 'Mantecol', 'precio': 750},
    {'id': 3, 'nombre': 'Coca-Cola', 'precio': 1000},
    {'id': 4, 'nombre': 'Takis', 'precio': 2500},
]

# Lista de productos comprados (Inicializa Vacia)
productos_comprados = []

# ------------------------
# Función para Mostrar Snacks disponibles
# ------------------------
def mostrar_snacks():
    print(f'\n[Productos Disponibles]\n')

    for producto in productos_maquina:
        print(f'ID: {producto.get("id")} -> {producto.get("nombre")} - $ {producto.get("precio")}')

# ------------------------
# Función para Comprar Snacks
# ------------------------
def comprar_snacks():
    # Variables Locales
    id_producto = int(input('\nIngresa el ID del snack: '))

    # Llamada a la función Buscar Productos
    producto_encontrado = buscar_producto(id_producto)

    if producto_encontrado is not None:
        productos_comprados.append(producto_encontrado)
        print(f'[+] Producto aregado: {producto_encontrado}')
    else:
        print(f'[!] Producto NO encontrado con el ID: {id_producto}')

# ------------------------
# Función para Mostrar Boleta
# ------------------------
def mostrar_boleta():
    print(f'\n[BOLETA ELECTRONICA]')
    
    # Variables Locales
    boleta = ''
    total = 0

    for producto in productos_comprados:
        boleta += f'- {producto.get("nombre")} \t${producto.get("precio")}\n'
        total += producto.get('precio')
    boleta += f'\nTOTAL: ${total}'

    print(boleta)


# Funcion buscar producto en la maquina
def buscar_producto(id_ingresado):
    for producto in productos_maquina:
        if producto.get('id') == id_ingresado:
            return producto
    # Si no encontro el producto en la maquina devolver None
    return None
        
# -------------------------------
# Testeando la aplicación
# -------------------------------
if __name__ == '__main__':
    while True:
        print(f'''
OPCIONES:
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
            print(f'\nSaliendo del programa...')
            break
        else:
            print(f'\n[!] Error, seleccione una opcion valida...')