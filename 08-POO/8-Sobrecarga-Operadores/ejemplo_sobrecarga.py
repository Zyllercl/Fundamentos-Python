
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    # Sobrecargar el metodo de suma
    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'
    
    # Sobrecargar el metodo resta
    def __sub__(self, other):
        return self.edad - other.edad

persona1 = Persona('Clarke', 26)
persona2 = Persona('Raven', 24)

print(persona1 + persona2)
print(persona1 - persona2)