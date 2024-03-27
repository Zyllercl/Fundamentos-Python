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
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)' # (%s) -> Son los valores a entregar
            values = ('Billy', 'Dawolf', 'billy@billy.es')  # Valores a ingresar para la sentencia anterior
            cursor.execute(sentencia, values) # Ejecuta la sentencia SQL con los valores VALUES
            # conexion.commit() # Se guardan los cambios en la db (Para este caso lo hace de manera automatica por el WITH)
            registros_insertados = cursor.rowcount
            print(f'[+] Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'[ERROR] Hubo un problema: {e}')
finally:
    # Cierre de la conexion a db
    conexion.close()