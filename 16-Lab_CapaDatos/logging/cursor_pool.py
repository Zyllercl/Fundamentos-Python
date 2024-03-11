# Resource o Context Manager

from logger_base import log
from conexion import Conexion


class CursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
    
    # Este metodo se mandara a llamar cuando se ocupe la sentencia with
    def __enter__(self): 
        log.debug(f'[+] Inicio del metodo with __enter__')
        self._conexion = Conexion.obtener_conexion() # Objeto de tipo conexion
        self._cursor = self._conexion.cursor() # Objeto de tipo cursor, encargado de ejecutar las sentencia a la db
        return self._cursor
    
    # Se ejecuta esta funcion cuando termina una sentencia with (es decir, cuando se termina de ejecutar una sentencia sql)
    def __exit__(self, type_except, value_exception, traceback_exception):
        log.debug(f'[+] Ejecucion del metodo __exit__')
        if value_exception: # Si existe una exepcion
            self._conexion.rollback() # Se ejecuta un rollback de la db
            log.error(f'[!] Ocurrio una excepcion, se realizo rollback: {value_exception} | {type_except} | {traceback_exception}')
        else:
            self._conexion.commit() # Se guardan los cambios en la db
            log.debug(f'[+] Se realizo un commit de la transaccion')
        
        self._cursor.close() # Se cierra el cursor
        Conexion.liberar_conexion(self._conexion) # Liberacion del objeto conexion
    
    
# TESTING #
if __name__ == '__main__':
    # Inicializacion del cursor
    with CursorPool() as cursor:
        log.debug(f'[*] Inicio bloque with...')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())