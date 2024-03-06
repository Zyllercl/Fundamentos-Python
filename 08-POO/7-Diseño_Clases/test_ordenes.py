from Producto import Producto
from Orden import Orden


# Crear productos
producto1 = Producto('Camisa', 2000)
producto2 = Producto('Pantalon', 3500)
producto3 = Producto('Calcetines', 1500)
producto4 = Producto('Poleron', 5600)

# Crear una lista de productos
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

# Crear una Orden
orden1 = Orden(productos1)
orden1.agregar_producto(producto3) # Agregamos un producto a la orden ya creada
print(orden1)

# Imprimir total
print(f'Total Orden: {orden1.calcular_total()}')

orden2 = Orden(productos2)
print(orden2)
print(f'Total Orden: {orden2.calcular_total()}')