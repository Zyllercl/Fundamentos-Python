from logger_base import log
from conexion import Conexion

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        # Inicializacion de los atributos
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        
    def __str__(self):
        return f'''
            ID Persona: {self._id_persona},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Correo: {self._email}
        '''
    
    # Metodo GET
    @property
    def id_persona(self):
        return self._id_persona
    # Metodo SET
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
    
    # Metodo GET
    @property
    def nombre(self):
        return self._nombre
    # Metodo SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    # Metodo GET
    @property
    def apellido(self):
        return self._apellido
    # Metodo SET
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    # Metodo GET
    @property
    def email(self):
        return self._email
    # Metodo SET
    @email.setter
    def email(self, email):
        self._email = email


# TESTING #
if __name__ == '__main__':
    persona1 = Persona(1, 'Coco', 'Lox', 'coco@coco.cl')
    log.debug(persona1)
    
    # Simulacion de un INSERT
    persona1 = Persona(nombre='Coco', apellido='Lox', email='coco@lox.cl')
    log.debug(persona1)
    
    # Simulacion de un DELETE
    persona1 = Persona(id_persona=1)
    log.debug(persona1)