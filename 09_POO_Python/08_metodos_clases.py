'''
    METODOS DE CLASE


    Def:
        - Son funciones que se definen dentro de una clase, y estan diseñadas para trabajar con los atributos y objetos de dicha clase.
        
        Métodos:

            * Método Estático: No recibe un argumento implícito. Es un método que esta vinculado a la clase y no al objeto de la clase. Además, no se puede acceder ni modificar el estado de la clase. 

            * Método Clase: Es un método que esta vinculado a la clase, es decir, tiene acceso al estado de la clase y puede modificar un estado de clase el cual se aplicará a todas las instancias (objetos) de la clase.

        - Para acceder a una 'variable de clase' se puede obtener mediante un Objeto, es decir, de un 'Contexto Dinámico' a 'Contexto Estático'. Pero no se puede acceder viceversa.
'''

# Creacion de una clase
class Persona:
    # Variables de Clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementar el valor del 'Atributo de Clase'
        Persona.contador_personas += 1
        
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar_persona(self):
        print(f'ID: {self.id} , Nombre: {self.nombre} , Apellido: {self.apellido}')
    
    # Método Estático: Obtener 'variables de clase' en los métodos [Forma 1]
    @staticmethod
    def get_contador_personas_estatico():
        print('\n[~] Método Estático')
        return Persona.contador_personas

    # Método Clase (RECOMENDADA): Esta forma es similar a una instancia de clase, es decir, se referencia a la clase (asi misma) con 'cls' [Forma 2]
    @classmethod
    def get_contador_personas_clase(cls):
        print(f'\n[~] Método Clase')
        return cls.contador_personas

if __name__ == '__main__':
    print('---  INFORMACION PERSONA  ---')
    # Creacion Persona 1
    persona1 = Persona('Maestro', 'Splinter')
    persona1.mostrar_persona()
    
    # Creacion Persona 2
    persona2 = Persona('Donatelo', 'Yoshi')
    persona2.mostrar_persona()

    # Obtener la cantidad de objetos de tipo persona creados
    print(f'\nContador objetos de Persona: {Persona.contador_personas}')
    
    # Accediendo al contador personas mediante el método estatico
    print(f'Contador objetos de Persona (estático): {Persona.get_contador_personas_estatico()}')

    # Accediendo al contador personas mediante el método de clase
    print(f'Contador objetos de Persona (clase): {Persona.get_contador_personas_clase()}')