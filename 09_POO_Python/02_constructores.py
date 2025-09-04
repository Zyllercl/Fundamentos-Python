"""
Uso de Constructores en Python
==============================
Este script muestra un ejemplo de cómo se ocupan los 'Constructores' en Python.
"""

# --------------------------------
# Creación de una Clase
# --------------------------------
class Persona:
    # --------------------------------
    # Creación del Constructor
    # --------------------------------
    def __init__(self, nombre, apellido):
        # --------------------------------
        # Creación de los Atributos de Instancia
        # --------------------------------
        self.nombre = nombre
        self.apellido = apellido 
    
    def mostrar_persona(self):
        print(f'''Datos Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        ''')
        
        # --------------------------------
        # Obtener Dirección de Memoria de Self
        # --------------------------------
        print(f'Dirección de Memoria Self: {id(self)}')
        print(f'Dirección de Memoria Hexadecimal Self: {hex(id(self))}\n')

# --------------------------------
# Testeando la Clase
# --------------------------------
if __name__ == '__main__':
    # --------------------------------
    # Creación del primer objeto (Instanciar una Clase)
    # --------------------------------
    persona = Persona('Bellamy', 'Blake')  # Se crea un objeto con los parametros para inicializar un objeto
    
    persona.mostrar_persona()              # Mostrar objeto de tipo Persona

    # --------------------------------
        # Obtener Dirección de Memoria del Objeto
        # --------------------------------
    print(f'Dirección de Memoria Persona: {id(persona)}')
    print(f'Dirección de Memoria Hexadecimal Persona: {hex(id(persona))}')