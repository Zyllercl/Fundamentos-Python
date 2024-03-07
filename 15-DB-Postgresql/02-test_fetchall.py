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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' # Sentencia SQL
            # llaves_primarias = ((1,2,3),) # Datos en duro
            entrada = input('Ingresa los ID\'s a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')), ) # Elimina todas las comas y los transforma a una tupla
            cursor.execute(sentencia, llaves_primarias) # Ejecutamos la sentencia SQL en la db
            registros = cursor.fetchall() # Recuperar todos los registros de la sentencia anteriormente enviada
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'[ERROR] Hubo un problema: {e}')
finally:
    # Cierre de la conexion a db
    conexion.close()