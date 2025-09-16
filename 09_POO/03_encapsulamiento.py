"""
Uso del Encapsulamiento en Python
=================================
Este script muestra el uso práctico de los tres niveles de encapsulamiento (público, protegido y privado) mediante una clase Auto, ilustrando las formas correctas e incorrectas de acceder a sus atributos.
"""

# --------------------------------
# Creación de una Clase de tipo Auto
# --------------------------------
class Auto:
    # --------------------------------
    # Creación del Constructor
    # --------------------------------
    def __init__(self, marca, modelo, color):
        # --------------------------------
        # Creación de los Atributos de Instancia
        # --------------------------------
        self.marca = marca          # Atributo Público (Default)
        self._modelo = modelo       # Atributo Protegido
        self.__color = color        # Atributo Privado

    # Mostrar Info del Auto
    def informacion(self):
        print(f'''\nInformación del Auto:
Marca: {self.marca}
Modelo: {self._modelo}
Color: {self.__color}
''')

# --------------------------------
# Testeando el Encapsulamiento
# --------------------------------
if __name__ == '__main__':
    # --------------------------------
    # Creación del primer objeto (Instanciar una Clase)
    # --------------------------------
    auto_kia = Auto('Kia', 'Rio', 'Plateado')
    auto_kia.informacion()

    # --------------------------------
    # Modificando la Data
    # --------------------------------
    auto_kia.marca = 'Kia 2'
    auto_kia._modelo = 'Rio 2'              # Los atributos protegidos NO SE DEBEN MODIFICAR
    auto_kia.__color = 'Plateado 2'         # Los atributos privados NO cambiaran su valor inicial
    auto_kia._Auto__color = 'Plateado 3'    # NO SE DEBE REALIZAR ESTA PRACTICA!!!
    auto_kia.informacion()