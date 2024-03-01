
# Herencia

"""
    Que es la Herencia?     -> La herencia consiste en que se puede crear una clase que sea 'hijo' o una 'copia' de otra, al heredar de una clase se tendra todos los 'metodos' y 'atributos' de la clase 'padre' en el hijo, y podras modificarlos en caso de ser necesario.
"""

# Definir una Clase
class Restaurant:
    # Constructor -> Se ejecuta automaticamente
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.__precio = precio # PROTECTED
        
    # Metodos
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')
    
    # Definicion de Getters y Setters | Get = Obtiene un valor - Set = Agrega un valor
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio

# Crear una clase hijo de restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        # Referencia a la clase padre
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 Estrellas', 300)
hotel.mostrar_informacion()