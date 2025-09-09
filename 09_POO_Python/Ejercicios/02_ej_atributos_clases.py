"""
Ejemplo: Atributos de Clases
============================
Este script muestra como se comportan los Atributos de Clases y Atributos de Instancia.
"""
# -----------------------------
# Creación de la Clase
# -----------------------------
class Persona:
    # -----------------------------
    # Variables de Clase
    # -----------------------------
    contador_personas = 0

    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(self, nombre, apellido):
        # -----------------------------
        # Incremento de la variable "contador_personas" (Atributo de Clase)
        # -----------------------------
        Persona.contador_personas += 1
        
        # -----------------------------
        # Atributos de Instancia
        # -----------------------------
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
    
    # -----------------------------
    # Métodos dentro de la Clase (Funciones)
    # -----------------------------
    def mostrar_persona(self):
        print(f'ID: {self.id} , Nombre: {self.nombre} , Apellido: {self.apellido}')

# -----------------------------
# Probando la Aplicación
# -----------------------------
if __name__ == '__main__':
    print('[ATRIBUTOS DE CLASES - ATRIBUTOS DE INSTANCIAS]\n')
    
    # -----------------------------
    # Creación del Objeto 1
    # -----------------------------
    persona1 = Persona('Peppa', 'Pig')
    persona1.mostrar_persona()
    
    # -----------------------------
    # Creación del Objeto 2
    # -----------------------------
    persona2 = Persona('Suzy', 'Sheep')
    persona2.mostrar_persona()

    # -----------------------------
    # Obtener la cantidad de objetos de tipo persona creados
    # -----------------------------
    print(f'\nContador objetos de Persona: {Persona.contador_personas}\n')