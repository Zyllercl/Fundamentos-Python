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
            # Valores a ingresar para la sentencia anterior
            values = (
                ('Billy', 'Dawolf', 'billy@billy.es'),
                ('Jimmy', 'Elque', 'jimy@jimycom'),
                ('Algos', 'Palgos', 'palgos@palgos.com')
            ) 
            cursor.executemany(sentencia, values) # Ejecuta la sentencia SQL con varios valores VALUES
            registros_insertados = cursor.rowcount
            print(f'[+] Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'[ERROR] Hubo un problema: {e}')
finally:
    # Cierre de la conexion a db
    conexion.close()