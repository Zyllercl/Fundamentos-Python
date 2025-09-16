"""
Uso de Métodos de Clase
=======================
Este script muestra como funciona el Método Estático y el Método de Clase en Python.
"""

# --------------------------------
# Creación de Clase de tipo Persona
# --------------------------------
class Persona:
    # --------------------------------
    # Creación de los Atributos de Clase
    # -------------------------------
    contador_personas = 0

    # --------------------------------
    # Creación del Constructor
    # -------------------------------
    def __init__(self, nombre, apellido):
        # --------------------------------
        # Modificación Atributo de Clase
        # -------------------------------
        Persona.contador_personas += 1  # Incrementa el valor del 'Atributo de Clase' (contador_personas)
        # --------------------------------
        # Creación de los Atributos de Instancia
        # -------------------------------
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
    
    # --------------------------------
    # Creación de Método de Instancia
    # -------------------------------
    def mostrar_persona(self):
        print(f'ID: {self.id} , Nombre: {self.nombre} , Apellido: {self.apellido}')
    
    # --------------------------------
    # Creación Método Estático
    # -------------------------------
    @staticmethod
    def get_contador_personas_estatico():
        print('\n[Método Estático]')
        # Retorna el valor de la "Variable de Clase" [Forma 1]
        return Persona.contador_personas
    
    # --------------------------------
    # Creación Método de Clase 
    # -------------------------------
    @classmethod
    def get_contador_personas_clase(cls):
        print(f'\n[Método de Clase]')
        # [RECOMENDADO] Método similar a una "Instancia de Clase", se referencia a la Clase (así misma) con 'cls' [Forma 2]
        return cls.contador_personas


if __name__ == '__main__':
    print('[INFORMACIÓN DE LA PERSONA]\n')

    # --------------------------------
    # Creación del Primer Objeto
    # -------------------------------
    persona1 = Persona('Pepe', 'Mujica')
    persona1.mostrar_persona()
    
    # --------------------------------
    # Creación del Segundo Objeto
    # -------------------------------
    persona2 = Persona('Donatelo', 'Yoshi')
    persona2.mostrar_persona()

    # --------------------------------
    # Obtener la cantidad de Objetos de tipo Persona creados
    # -------------------------------
    print(f'\nContador objetos de Persona: {Persona.contador_personas}')
    
    # --------------------------------
    # Acceder al Contador Personas mediante el Método Estático
    # -------------------------------
    print(f'Contador objetos de Persona (estático): {Persona.get_contador_personas_estatico()}')

    # --------------------------------
    # Acceder al Contador Personas mediante el Método Clase
    # ------------------------------- 
    print(f'Contador objetos de Persona (clase): {Persona.get_contador_personas_clase()}')