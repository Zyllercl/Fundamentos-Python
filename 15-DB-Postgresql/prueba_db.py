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

cursor = conexion.cursor() # Creamos un cursos hacia la conexion a la db
sentencia = 'SELECT * FROM persona' # Sentencia SQL
cursor.execute(sentencia) # Ejecutamos la sentencia SQL en la db
registros = cursor.fetchall() # Recuperar todos los registros de la sentencia anteriormente enviada
print(registros)

# Cierre de la conexion a db
cursor.close()
conexion.close()