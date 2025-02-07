'''
    CREAR UNA CLASE EN PYTHON
'''

# Definicion de una clase
class Persona:
    
    def inicializar_persona(self, nombre, apellido):
        # Creación de atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Datos Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        ''')

# Creación de Objetos
if __name__ == '__main__':
    # Creacion del primer objeto
    persona1 = Persona() # Se crea un objeto vacio en memoria
    persona1.inicializar_persona('Bellamy', 'Blake') # Creacición de una Persona (Objeto)
    persona1.mostrar_persona() # Mostrar objeto de tipo Persona

    # Creacion del segundo objeto
    persona2 = Persona()
    persona2.inicializar_persona(nombre='Jhon', apellido='Snow')
    persona2.mostrar_persona()