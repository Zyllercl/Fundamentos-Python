
# Ejercicio: Por cada Objeto que se crea, se le asignara un ID unico

class Persona:
    # Variables Globales
    contador_persona = 0
    
    # Metodo de clase
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona
    
    def __init__(self, nombre, edad):
        Persona.generar_siguiente_valor()
        
        # Atributos
        self.id_persona = Persona.contador_persona
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona [ID: {self.id_persona}, Nombre: {self.nombre}, Edad: {self.edad}]'


# Crear un objeto tipo persona
persona = Persona('Bellamy', 30)
print(persona)

persona2 = Persona('Clarke', 34)
print(persona2)

persona3 = Persona('Raven', 32)
print(persona3)

Persona.generar_siguiente_valor()

persona4 = Persona('Jhon', 35)
print(persona4)

print(f'Valor contador personas: {Persona.contador_persona}')