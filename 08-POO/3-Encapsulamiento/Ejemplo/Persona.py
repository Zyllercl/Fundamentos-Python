
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # PROTECTED, no se debe alterar el valor de esta variable
        self.__apellido = apellido # PRIVATE, se puede acceder a la variable por fuera de la clase, solo se puede acceder mediante un metodo
        self.edad = edad

    """
        Metodo get -> Obtener/Recuperar informacion de una variable
        Metodo set -> Modificar/Cambiar informacion de una variable

        Para dejar una variable de solo lectura (read only) se debe comentar el metodo setter.

        Decoradores
            @property -> Permite obtener el valor de una variable y este se podrá obtener a traves de un metodo como un atributo.
            @setter   -> Decorador setter permite cambiar el valor de una variable.
    """
    # Metodo get para obtener el nombre
    @property
    def get_nombre(self):
        print('Obteniendo nombre...')
        return self._nombre

    @get_nombre.setter
    def set_nombre(self, nombre):
        print('Llamando metodo set')
        self.nombre = nombre

    def mostrar_informacion(self):
        print('Obteniendo informacion general...')
        print(f'Persona [Nombre: {self._nombre} {self.__apellido}, Edad: {self.edad}]')
    
    # Metodo destructor (eliminar)
    def __del__(self):
        print(f'Persona: {self._nombre} {self.__apellido}')

# Evitar que se ejecute codigo de prueba cuando es llamado de otro archivo
if __name__ == '__main__':
    persona = Persona('Bellamy', 'Blake', 30)
    persona.mostrar_informacion()

    # Obtener nombre como atributo (gracias al decorador @property)
    # print(persona.get_nombre)

    # Cambiando el nombre con metodo set_nombre (Decorador setter)
    persona.set_nombre = 'Octavia'
    print(persona.nombre)

