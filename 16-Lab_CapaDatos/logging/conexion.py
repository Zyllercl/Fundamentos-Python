from logger_base import log
from  psycopg2 import pool
import sys

""" 
    Psycopg2 - Pool de Conexiones
    
    Definicion:
        -> Es un objeto que administra los objetos de conexion a la base de datos
        -> Cada pool de conexion va ha administrar una cantidad de objetos de conexion hacia la Base de Datos
            -> Cada cliente debe tener un pool de conexion a la base de datos
                -> Cuando un cliente termina de realizar sus QUERYS el ''objeto'' de conexion vuelve al pool para quedar habilitado para otro cliente
        -> Para crear un pool de conexiones se necesita un minimo y un maximo de 'objetos' de tipo conexion
"""

class Conexion:
    # Variables Globales PRIVADAS
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5434'
    _HOST = '127.0.0.1'
    _MIN_CON = 1 # Minimo de conexiones
    _MAX_CON = 5 # Maximo de conexiones
    _pool = None
    
    
    # Metodos de Clase #
    
    # Metodo para Obtener una pool de conexiones
    @classmethod
    def obtener_pool(cls): 
        # Configuracion de Conexiones
        if cls._pool is None:
            # Inicializacion de la variable pool
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
                log.debug(f'Creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'[!] Ocurrio un error al obtener el pool: {e}')
                sys.exit() # Termina el programa
        else:
            # Retorna el pool si ya existe
            return cls._pool
    
    @classmethod # Permiten acceder a las variables globales y modificarlo
    def obtener_conexion(cls):
        # Variables Locales del metodo
        conexion = cls.obtener_pool().getconn() # Obtenemos un objeto a la conexion a la base de datos
        log.debug(f'[+] Conexion obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion) # Regresa el objeto de conexion al pool de conexiones
        log.debug(f'[-] Regresando el objeto conexion al pool: {conexion}')
    
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall() # Todos los objetos de conexion del pool se cerraran


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