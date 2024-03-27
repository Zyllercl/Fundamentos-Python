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
            # Variables
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s' # Sentencia SQL para eliminar VARIOS registros
            entrada = input('Ingresa los id_persona a eliminar (separado por comas): ')
            values = (tuple(entrada.split(',')),) # Metodo split -> Regresa una lista, para convertirla en una tupla
            cursor.execute(sentencia, values) # Ejecuta la sentencia SQL con varios valores VALUES
            registros_eliminados = cursor.rowcount
            print(f'[+] Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'[ERROR] Hubo un problema: {e}')
finally:
    # Cierre de la conexion a db
    conexion.close()