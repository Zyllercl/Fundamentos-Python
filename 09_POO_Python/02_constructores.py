'''
    CONSTRUCTORES EN PYTHON

    Def:
        - Un constructor es un 'método especial' y se utiliza para 'crear un objeto' o instanciar una clase. Además, puede servir para crear e inicializar los atributos de un nuevo objeto
        
            - Sintaxis Constructur
                
                class NombreDeLaClase:
                    def __init__(self, parametro1, parametro2):
                        self.parametro1 = parametro1
                        self.parametro2 = parametro2

                    Donde:
                        - __init__():   El método init (inicializador) se conoce como un método de tipo dunder (doble underscore)

    DIRECCION DE MEMORIA

    Def:
        - Cuando se crea un 'objeto', este se almacena ocupando un espacio en la memoria (ej: 0x311...)
        - La variable 'self' toma como referencia el 'objeto' actual con el que se interactua, es decir, que tomará el valor de memoria donde esta guardado el 'objeto'

        Obtener direccion de memoria: id(variable)
        Obtener direccion de memoria hexadecimal: hex(id(variable))
'''

'''     USO DE CONSTRUCTORES    '''

# Ejemplo de un constructor
class Persona:
    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido 
    
    def mostrar_persona(self):
        print(f'''Datos Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        ''')
        
        # Obtener direccion de memoria de self
        print(f'Dirección de Memoria Self: {id(self)}')
        print(f'Dirección de Memoria Hexadecimal Self: {hex(id(self))}\n')

# Creación de Objetos
if __name__ == '__main__':
    # Creacion del primer objeto
    persona1 = Persona('Bellamy', 'Blake') # Se crea un objeto con los parametros para inicializar un objeto
    persona1.mostrar_persona() # Mostrar objeto de tipo Persona

    # Obtener el ID del objeto
    print(f'Dirección de Memoria Persona1: {id(persona1)}')
    print(f'Dirección de Memoria Hexadecimal Persona1: {hex(id(persona1))}')