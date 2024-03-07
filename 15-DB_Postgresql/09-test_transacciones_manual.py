""" 
    1.- Primero se debe crear un entorno virtual para manejar Postgresql
        1.1.- Comando para crear un entorno virtual:
            > python -m venv .venv
        1.2.- Activar Entorno Virtual
            > cd .venv\Scripts
            > activate
        1.3.- Actualizar en Entorno Virtual
            > python -m pip install --upgrade pip
    2.- Instalar Psycopg2
        > python3 -m pip install psycopg2-binary
"""

import psycopg2 as db

# Conexion a la Base de Datos Postgresql
conexion = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5434',
    database='test_db'
)

# Crear conexion
try:
    # Metodo Manual Transacciones
    """ 
    - Una transaccion ejecuta todas las sentencia si todas fueron correctas
    - Las sentencia a utilizar en las transacciones son: INSERT | UPDATE | DELETE
    conexion.autocommit = False # No se realizan cambios en la db hasta terminar la transaccion
    conexion.autocommit = True # No recomendable ya que se guardaran los cambios en la db aun si hay errore
    
    
    """
    # Inicio de la transaccion
    conexion.autocommit = False
    
    # Insercion de un solo registro en la db
    cursor = conexion.cursor() # Inicializamos cursor
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)' # Sentencia SQL para insertar un nuevo registro
    values = ('Billy','Dawolf','billy@billy.cl') # Valores a la sentencia SQL anterior
    cursor.execute(sentencia, values) # Ejecucion de la sentencia SQL
    
    # Actualizacion de un solo registro en la db
    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    values = ('Jimy', 'Elkeso', 'elque@elque.cl', 9)
    cursor.execute(sentencia, values)
    
    # Actualizacion de la base de datos
    conexion.commit()
    print('[-] Terminando la transaccion, se realizo un commit!')
except Exception as e:
    conexion.rollback() # Roolback -> Devuelve los valores antes de la consulta SQL
    print(f'[ERROR] Hubo un problema, se hizo rollback de la transaccion: {e}')
finally:
    # Cierre de la conexion a db
    conexion.close()