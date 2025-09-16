"""
Polimorfismo en Python
=====================
Este script muestra un ejemplo de la estructura y como funciona el Polimorfismo en Python.
"""

# Funcion Polimorfica (Recibira distintos tipos de datos)

# --------------------------------
# Creación de Clase Padre (Superclase)
# --------------------------------
class Animal:
    # --------------------------------
    # Métodos de la Clase Padre
    # --------------------------------
    def hacer_sonido(self):
        print(f'Sonido no identificado!')
    
# --------------------------------
# Creación de Clase Hija (Subclase)
# --------------------------------
class Perro(Animal):
    # --------------------------------
    # Sobreescritura del Método Padre
    # --------------------------------
    def hacer_sonido(self):
        print(f'Guau Guau')

class Gato(Animal):
    # --------------------------------
    # Sobreescritura del Método Padre
    # --------------------------------
    def hacer_sonido(self):
        print(f'Miau Miau')

class Tortuga(Animal):
    pass

# --------------------------------
# Función Polimorfica: función que recibirá distintos tipos de datos
# --------------------------------
def hacer_sonido_animal(animal):
    # Concepto Duck Typing: Si parece 'pato' y se comporta como 'pato', entonces es un pato.
    # Si el parametro entregado es de tipo "perro", entonces entrará en la función de la clase "Perro".
    animal.hacer_sonido()

# --------------------------------
# Testing Polimorfismo
# --------------------------------
print(f'\n[USO POLIMORFISMO]\n')

print(f'(Clase Padre)')
animal = Animal()
animal.hacer_sonido()   # Método Padre (Original)

print(f'\n(Clase Hija - Perro)')
perro = Perro()
perro.hacer_sonido()    # Método Hijo de Perro (Polimorfismo)

print(f'\n(Clase Hija - Gato)')
gato = Gato()
gato.hacer_sonido()     # Método Hijo de Gato (Polimorfismo )

print(f'\n(Clase Hija - Tortuga)')
tortuga = Tortuga()
tortuga.hacer_sonido()  # Método Hijo de Tortuga (No Aplica Polimorfismo)


# --------------------------------
# Testing Funcion Polimorfica
# --------------------------------
print(f'\n[USO FUNCION POLIMORFICA]\n')

print(f'(Animal)')
hacer_sonido_animal(animal)

print(f'\n(Perro)')
hacer_sonido_animal(perro)

print(f'\n(Gato)')
hacer_sonido_animal(gato)

print(f'\n(Tortuga)')
hacer_sonido_animal(tortuga)