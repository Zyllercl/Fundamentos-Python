
# Abstracciones y Constructores

"""
    Abstraccion     -> Son los datos necesarios de una Clase
        Ej: Si se elabora un menu de un restaurant es necesario el 'nombre del plato', 'descripcion', 'precio'
"""

# Definir una Clase
class Restaurant:
    # Constructor -> Se ejecuta automaticamente
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio

    # Metodos
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

# Instanciar la clase
restaurant = Restaurant('Pizzeria', 'Pizza Tradicional', 3000) 
restaurant.mostrar_informacion() # Llamando a un metodo

restaurant2 = Restaurant('Hamburgeseria', 'Hamburgesa Tocino', 4500)
restaurant2.mostrar_informacion()