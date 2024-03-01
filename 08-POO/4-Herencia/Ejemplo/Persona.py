
# Clase Padre
class Persona:
    # Constructor -> Se ejecuta automaticamente
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributo
        self.edad = edad
    
    # Metodos
    def __str__(self):
        # Sobreescribiendo
        return f'Persona [Nombre: {self.nombre}, Edad: {self.edad}]'

# Crear una clase hijo de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) # Accediendo a los metodos de la clase padre (Persona)
        self.sueldo = sueldo
    
    def __str__(self):
        return f'Empleado [Sueldo: {self.sueldo}] {super().__str__()}'