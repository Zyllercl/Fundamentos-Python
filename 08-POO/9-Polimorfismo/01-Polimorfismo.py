
# Polimorfirmo POO

"""
    Que es el polimorfismo      -> Es la habilidad de tener diferentes comportamientos basados en que clase o subclase se esta utilizando, esta relacionado estrechamente con Herencia
"""

# Definir una Clase
class Restaurant:
    # Constructor -> Se ejecuta automaticamente
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio # PROTECTED
        
    # Metodos
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')
    
    # Definicion de Getters y Setters | Get = Obtiene un valor - Set = Agrega un valor
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio

# Crear una clase hijo de restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, piscina):
        # Referencia a la clase padre (constructor)
        super().__init__(nombre, categoria, precio)
        # Agregar un nuevo atributo especifico para la clase Hotel
        self.piscina = piscina
    
    # Reescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Piscina: {self.piscina}')

    # Agregar un metodo que solo exista en hotel (Polimorfismo)
    def get_piscina(self):
        return self.piscina

hotel = Hotel('Hotel POO', '5 Estrellas', 300, 'Si')
hotel.mostrar_informacion()
piscina = hotel.get_piscina()