
""" 
    Definicion DAO (Data Access Object): Es un Patron de Diseño para comunicarse con una Base de Datos
    
    Creacion de un CRUD: Create | Read | Update | Delete
"""
from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_pool import CursorPool


class PersonaDAO:
    # Variables Globales PRIVADAS
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
    
    # Metodos de Clases
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor: # Obtenemos el cursor de la clase CursorPool
            cursor.execute(cls._SELECCIONAR) # Ejecuta la sentencia SQL _SELECCIONAR
            registros = cursor.fetchall() # Recuperar todos los registros de la db
            personas = [] # LISTA PERSONAS
            
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3]) # Se transforman los registros en objetos de tipo persona
                personas.append(persona) # Se agrega a la lista un objeto de tipo persona
            return personas
    
    @classmethod
    def insertar(cls, persona):
        # Creamos una transaccion
        with CursorPool() as cursor: # Obtenemos el cursor de la clase CursorPool
            values = (persona.nombre, persona.apellido, persona.email) 
            cursor.execute(cls._INSERTAR, values) # Ejecucion SQL para insertar una nueva persona
            log.debug(f'[+] Persona agregada: {persona}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona):
        # Creamos una transaccion
        with CursorPool() as cursor: # Obtenemos el cursor de la clase CursorPool
            values = (persona.nombre, persona.apellido, persona.email, persona.id_persona) # Tupla de Valores que se ingresaran a la db
            cursor.execute(cls._ACTUALIZAR, values) # Ejecucion sentencia SQL de actualizar una persona
            log.debug(f'[+] Persona actualizada: {persona}')
            return cursor.rowcount # Devuelve la cantidad de objetos que fueron modificados en la db
            # No es necesario hacer un commit ya que lo hace automaticamente el with
    
    @classmethod
    def eliminar(cls, persona):
        with CursorPool() as cursor: # Obtenemos el cursor de la clase CursorPool
            values = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, values) # Ejecucion sentencia SQL de eliminar una persona
            log.debug(f'[-] Persona eliminada: {persona}')
            return cursor.rowcount # Devuelve la cantidad de objetos que fueron eliminados de la db
    
    
# TESTING #
if __name__ == '__main__':
    # Insertar un registro
    persona1 = Persona(nombre='Fifon', apellido='Trifon', email='fifo@fifo.cl')
    persona_insertadas = PersonaDAO.insertar(persona1) # Se agrega una nueva persona con la funcion 'insertar'
    log.debug(f'[+] Personas insertadas: {persona_insertadas}') # LOG
    
    # Actualizar un registro
    persona1 = Persona(11, 'Chalo', 'Bless', 'chalo@chalo.cl')
    personas_actualizadas = PersonaDAO.actualizar(persona1) # Se actualiza una persona ya creada con la funcion 'actualizar'
    log.debug(f'[-] Personas actualizadas: {personas_actualizadas}')
    
    # Eliminar un registro
    persona1 = Persona(id_persona=16) # Para entregar 1 solo valor al objeto Persona se debe escribir el atributo a modificar
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'[-] Personas eliminadas: {personas_eliminadas}')
    
    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)