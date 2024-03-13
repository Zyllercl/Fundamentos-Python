
from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    # Variables Globales PRIVADAS
    _DATABASE = 'lab_usuarios'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5434'
    _HOST = '127.0.0.1'
    _MIN_CON = 1 # Minimo de conexiones
    _MAX_CON = 5 # Maximo de conexiones
    _pool = None
    
    # Metodos de clase
    @classmethod
    def obtener_pool_conexiones(cls):
        if cls._pool is None:
            # Conexion a la db
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._DB_PORT,
                    database = cls._DATABASE
                )
                # log.debug(f'[+] Creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'[!] Ocurrio un error al obtener el pool: {e}')
                sys.exit() # Termina el programa
        else:
            return cls._pool # Retorna el pool si ya existe
    
    @classmethod
    def obtener_conexion(cls):
        # Variables Locales
        connection = cls.obtener_pool_conexiones().getconn() # Obtencion de un objeto a la conexion a la db
        # log.debug(f'[+] Conexion obtenida del pool (objeto): {connection} ')
        return connection
    
    @classmethod
    def liberar_conexion(cls, connection):
        cls.obtener_pool_conexiones().putconn(connection) # Regresa el objeto conexion al pool de conexiones
        # log.debug(f'[+] Agregando el objeto al pool de conexiones: {connection}')
    
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool_conexiones().closeall() # Todos los objetos de conexion del pool se cerraran


# TESTING #
if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion() # Uso del objeto de 'conexion'
    Conexion.liberar_conexion(conexion1) # Se libera el objeto de 'conexion' hacia el pool de conexiones
    conexion2 = Conexion.obtener_conexion() # Uso del objeto de 'conexion' identico al de 'conexion1'
    # Obtener objetos de conexion
    conexion3 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion3) # Se libera el objeto de 'conexion' hacia el pool de conexiones
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion5) # Se libera el objeto de 'conexion' hacia el pool de conexiones
    conexion6 = Conexion.obtener_conexion()