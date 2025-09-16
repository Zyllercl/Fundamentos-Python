"""
Creación de una Clase en Python
===============================
Este script muestra los fundamentos de la creación de 'Clases' y 'Objetos'.
"""

# --------------------------------
# Creación de una Clase
# --------------------------------
class Persona:
    # --------------------------------
    # Creación de Métodos
    # --------------------------------
    def inicializar_persona(self, nombre, apellido):
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
# Testeando la Clase
# --------------------------------
if __name__ == '__main__':
    # --------------------------------
    # Creación del primer objeto (Instanciar una Clase)
    # --------------------------------
    persona1 = Persona()                                # Se crea un objeto vacio en memoria

    persona1.inicializar_persona('Bellamy', 'Blake')    # Creación de una Persona (Objeto)

    persona1.mostrar_persona()                          # Mostrar objeto de tipo Persona

    # --------------------------------
    # Creación del segundo objeto
    # --------------------------------
    persona2 = Persona()
    persona2.inicializar_persona(nombre='Jhon', apellido='Snow')
    persona2.mostrar_persona()