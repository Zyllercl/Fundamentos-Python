'''
    ENCAPSULAMIENTO EN PYTHON

    Def:
        - El encapsulamiento nos permite ocultar la información que almacena un objeto, conocido como el 'estado del objeto', es decir, el encapsulamiento permite restringuir u ocultar el acceso a los datos dentro de la misma clase del mundo exterior (usualmente se modifican via metodos en la misma clase)

            Tipos de encapsulamiento:
                    ->  PUBLIC       : Default
                    -> _PROTECTED    : No se puede alterar el valor de la variable
                    -> __PRIVATE     : Se puede acceder a la variable por fuera de la clase, solo se puede acceder mediante un método

    Caracteristicas del encapsulamiento:
        
        1. Atributos protegidos o privados

            self._nombre    -> Atributo Protegido 
            self.__nombre   -> Atributo Privado
        
        2. Crear los métodos conocidos como Get (leer) y Set (modificar)

            - Método GET -> Obtener/Recuperar información de una variable
            - Método SET -> Modificar/Cambiar información de una variable
            
            [!] Las funciones GET y SET sólo seran necesarias para acceder a los atributos dentro de la clase, si los atributos se llaman dentro de la misma clase, no es necesario declarar los GET y SET respectivamente.

            [!] Para dejar una variable de solo lectura (read only) se debe comentar el método setter.

            Decoradores:
                @property -> Permite obtener el valor de una variable y este se podrá obtener a traves de un método como un atributo.
                @setter   -> Decorador setter permite cambiar el valor de una variable.
'''

# Definicion de la clase auto
class Auto:

    # Constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca      # Atributo Default (Público)
        self._modelo = modelo   # Atributo Protegido
        self.__color = color    # Atributo Privado

    # Mostrar info del auto
    def informacion(self):
        print(f'''\nInformación del Auto
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}
        ''')

# Programa Principal
if __name__ == '__main__':
    # Creacion del primer objeto
    auto_kia = Auto('Kia', 'Rio', 'Plateado')
    auto_kia.informacion()

    # Cambiando la data
    auto_kia.marca = 'Kia 2'
    auto_kia._modelo = 'Rio 2'              # Los atributos protegidos NO SE DEBEN MODIFICAR
    auto_kia.__color = 'Plateado 2'         # Los atributos privados NO cambiaran su valor inicial
    auto_kia._Auto__color = 'Plateado 2'    # NO SE DEBE REALIZAR ESTA PRACTICA!!!
    auto_kia.informacion()