
class Producto:
    # Variable de clase
    contador_productos = 0
    
    def __init__(self, nombre, precio) -> None:
        Producto.contador_productos += 1
        
        # Atributos
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
        
    # Metodos Get y Sett (Ya que son atributos PROTECTED, es decir que no se puede alterar el producto)
    
    # Metodo GET para Precio
    @property
    def precio(self):
        return self._precio
    
    
    def __str__(self) -> str:
        return f'ID Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

# Esto se ejecutara siempre y cuando se ejecute archivo en el mismo modulo (archivo)
if __name__ == '__main__':
    # Crear productos
    producto1 = Producto('Camisa', 2.000)
    print(producto1)
    producto2 = Producto('Pantalon', 3.500)
    print(producto2)