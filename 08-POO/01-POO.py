
# Programacion Orientada a Objetos (POO)

"""
    Cuando se define una clase deberás describir el comportamiento y forma de ese objeto
    El Objeto es la forma de referirse a la información creada por una clase (Instancia de una clase)
    Cada instancia de la clse tendrá la misma "forma" pero diferente información

    Terminología

    Clase               -> La forma que va a tener la información
    Objeto              -> Los datos unicos de cada uno 
    Instancia           -> El objeto que es creado al llamar una clase
    Atributo de Clase   -> Es una propiedad que tendran todos los objetos creados con nuestras clases
    Metodo              -> Es una funcion que existe dentro de una Clase
"""

# Definir una Clase
class Restaurant:
    # Metodos
    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

# Instanciar la clase
restaurant = Restaurant()
# Llamando a un metodo
restaurant.agregar_restaurant('Pizzeria')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Italiani')
restaurant2.mostrar_informacion()

# Mostrar la informacion
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')