

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