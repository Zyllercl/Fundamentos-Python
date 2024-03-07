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
            # Variables
            sentencia = 'DELETE FROM persona WHERE id_persona=%s' # Sentencia SQL para eliminar UN SOLO registro
            entrada = input('Ingresa la id_persona a eliminar: ')
            values = (entrada,) # ID a eliminar
            cursor.execute(sentencia, values) # Ejecuta la sentencia SQL con varios valores VALUES
            registros_eliminados = cursor.rowcount
            print(f'[+] Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'[ERROR] Hubo un problema: {e}')
finally:
    # Cierre de la conexion a db
    conexion.close()