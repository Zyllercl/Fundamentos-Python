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
    # --------------------------------
    # Métodos de la Clase Hija
    # --------------------------------
    def hacer_sonido(self):
        print(f'Guau Guau')

    # --------------------------------
    # Sobreescritura (Override)
    # --------------------------------
    # Sobreescritura del Método dormir() (El nuevo método se debe llamar igual al método Padre)
    def dormir(self):
        print(f'Duermo 10 horas al día')

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
perro_1.dormir()    # Se llama el método sobreescrito en la Clase Hija
perro_1.hacer_sonido()
