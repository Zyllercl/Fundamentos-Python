
# Encapsulamiento
"""
    Encapsulamiento     -> Permite restringuir u ocultar el acceso a los datos dentro de la misma clase del mundo exterior (usualmente se modifican via metodos en la misma clase)
                        -> PUBLIC       : Default
                        -> _PROTECTED   : No se puede alterar el valor de la variable
                        -> __PRIVATE    : Se puede acceder a la variable por fuera de la clase, solo se puede acceder mediante un metodo
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

#   Restaurant 1   #
restaurant = Restaurant('Pizzeria', 'Pizza Tradicional', 3000) # Instanciar la clase
# restaurant.__precio = 2500 # No se puede modificar una variable cuando es definida PRIVATE
restaurant.mostrar_informacion() # Llamando a un metodo
restaurant.set_precio(2500)
precio = restaurant.get_precio()
print(precio)

#   Restaurant 2   #
restaurant2 = Restaurant('Hamburgeseria', 'Hamburgesa Tocino', 4500)
restaurant2.mostrar_informacion()
restaurant2.set_precio(6000)
restaurant2.get_precio()