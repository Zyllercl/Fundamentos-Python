import psycopg2

# Conexion a la Base de Datos Postgresql
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5434',
    database='test_db'
)

# Crear conexion
try:
    with conexion:
        with conexion.cursor() as cursor: # Creamos un cursos hacia la conexion a la db
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' # Sentencia SQL
            id_persona = input('Ingresa un ID de persona: ') # Variable con la id persona (Agregar en la sentencia SQL %s)
            # Para pasar un id_persona a la ejecucion de la sentencia se debe entregar en formato de tupla (Agregar al execute (id_persona,))
            cursor.execute(sentencia, (id_persona,)) # Ejecutamos la sentencia SQL en la db
            registros = cursor.fetchall() # Recuperar todos los registros de la sentencia anteriormente enviada
            # registros = cursor.fetchone() # Recupera solo un registro
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'[ERROR] Hubo un problema: {e}')
finally:
    # Cierre de la conexion a db
    conexion.close()