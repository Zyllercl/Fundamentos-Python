from Producto import Producto

class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos) -> None:
        Orden.contador_ordenes += 1
        
        # Atributos
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)
    
    # Agregar un producto de manera independiente
    def agregar_producto(self, producto):
        self._productos.append(producto) # Se agrega al final de la lista
    
    # Metodo para calcular el precio total de la orden
    def calcular_total(self):
        total = 0
        
        for producto in self._productos:
            total += producto.precio
    
        return total

    def __str__(self) -> str:
        # Almacena el __str__ de la clase Producto por cada producto
        productos_str = ''
        
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '
        
        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'

if __name__ == '__main__':
    # Crear productos
    producto1 = Producto('Camisa', 2000)
    producto2 = Producto('Pantalon', 3500)
    
    # Crear una lista de productos
    productos1 = [producto1, producto2]
    
    # Crear una Orden
    orden1 = Orden(productos1)
    print(orden1)
    
    orden2 = Orden(productos1)
    print(orden2)