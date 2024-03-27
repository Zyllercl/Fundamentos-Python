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
    # Metodo Automatico Transacciones
    with conexion:
        with conexion.cursor() as cursor:
            # Insercion de un solo registro en la db
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)' # Sentencia SQL para insertar un nuevo registro
            values = ('Mario','Gutsy','mario@mario.cl') # Valores a la sentencia SQL anterior
            cursor.execute(sentencia, values) # Ejecucion de la sentencia SQL
            
            # Actualizacion de un solo registro en la db
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            values = ('Algos', 'Palgos', 'algo@algo.cl', 10)
            cursor.execute(sentencia, values)
except Exception as e:
    # No es necesario agregar el rollback ya que se hace automatico
    print(f'[ERROR] Hubo un problema, se hizo rollback de la transaccion: {e}')
finally:
    # Cierre de la conexion a db
    conexion.close()
    
print('[-] Terminando la transaccion, se realizo un commit!')