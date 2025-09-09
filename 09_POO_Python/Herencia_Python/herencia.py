"""
Herencia en Python
==================
Este script muestra un ejemplo de la estructura y como funciona la Herencia en Python.
"""

# --------------------------------
# Creación de Clase Padre (Superclase)
# --------------------------------
class Animal:
    # --------------------------------
    # Métodos de la Clase Padre
    # --------------------------------
    def comer(self):
        print(f'Como muchas veces al día')

    def dormir(self):
        print(f'Duermo muchas horas')
    
# --------------------------------
# Creación de Clase Hija (Subclase)
# --------------------------------
class Perro(Animal):
    def hacer_sonido(self):
        print(f'Guau Guau')
    
# --------------------------------
# Testing Herencia
# --------------------------------
print(f'[EJEMPLO DE HERENCIA]\n')

print(f'[CLASE PADRE - MÉTODOS]')
animal_1 = Animal()
# Métodos de la Clase Padre
animal_1.comer()
animal_1.dormir()

print(f'\n[CLASE HIJA - MÉTODOS]')
perro_1 = Perro()
# Métodos de la Clase Padre e Hija
perro_1.comer()
perro_1.dormir()
perro_1.hacer_sonido()
