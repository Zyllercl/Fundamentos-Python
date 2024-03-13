from logger_base import log
from conexion_db import Conexion

class Cursor:
    def __init__(self):
        self._connection = None
        self._cursor = None
    
    def __enter__(self):
        # print('[!] Iniciando el metodo with __enter__')
        self._connection = Conexion.obtener_conexion() # Objeto tipo conexion
        self._cursor = self._connection.cursor() # Cursor obtenido del objeto conexion
        return self._cursor # Retornamos el cursor
    
    def __exit__(self, type_except, value_exception, tracback_exception):
        # print('[!] Iniciando el metodo __exit__')
        
        if value_exception:
            self._connection.rollback() # Se ejecuta rollback en la db
            log.error(f'[!] ERROR, se realizo rollback: {value_exception} | {type_except} | {tracback_exception}')
        else:
            self._connection.commit() # Se guardan los cambios en la db
            log.debug(f'[!] Se realizo un commit a la db')
        
        self._cursor.close() # Se cierra el cursor
        Conexion.liberar_conexion(self._connection) # Liberacion del objeto conexion hacia el pool de conexiones



# TESTING #
if __name__ == '__main__':
    # Inicializacion del cursor
    with Cursor() as cursor:
        print('[!] Inicio bloque with...')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())