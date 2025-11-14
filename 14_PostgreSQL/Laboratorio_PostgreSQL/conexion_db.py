"""
Desarrollo de un CRUD en PostgreSQL con Python y el módulo psycopg2 (También funciona con psycopg).
"""

# Importando el módulo psycopg2 para conectarse a PostgreSQL
import psycopg2

try:
    with psycopg2.connect(
        # Estableciendo la conexión a la base de datos PostgreSQL
        user="postgres", password="postgres",
        host="localhost", port="5432", database="test_db"
    ) as conexion:
        print(f'\n[INFO] Conexión exitosa...\n')

        # Creación de un cursor para ejecutar comandos SQL
        with conexion.cursor() as cursor:
            # --------------------------
            # OPERACIÓN CRUD SQL - INSERT
            # --------------------------
            sentencia_insert = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'

            # Ingresar 1 sólo registro
            valor_insert = ('Lara', 'Perez', 'lperez@email.cl')

            # Ingresar varios registros (en forma de tuplas dentro de una tupla)
            valores_insert = (
                ('Atenea', 'Rosas', 'arosas@email.cl'),
                ('Carlos', 'Nicols', 'cnicols@email.cl'),
                ('Gustavo', 'Reyes', 'greyes@email.com')
            )

            # --------------------------
            # Ejecutando la sentencia INSERT
            # --------------------------
            # cursor.execute(sentencia_insert, valor_insert)               # Insertar 1 solo registro
            # cursor.executemany(sentencia_insert, valores_insert)         # Insertar varios registros

            # Obtener el número de registros insertados
            registros_insertados = cursor.rowcount

            # print(f'[INFO] Registros Insertados: {registros_insertados}\n')

            # --------------------------
            # OPERACIÓN CRUD SQL - UPDATE
            # --------------------------
            sentencia_update = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'

            # Actualizar 1 sólo registro
            valor_update = ('Antonia', 'Reyes', 'areyes@email.cl', 4)

            # Actualizar varios registros (en forma de tuplas dentro de una tupla)
            valores_update = (
                ('Juana', 'Arcos', 'jarcos@email.cl', 1),
                ('Pedro', 'Pascal', 'ppascal@email.cl', 2),
                ('Laura', 'Tapia', 'ltapia@email.cl', 3)
            )

            # --------------------------
            # Ejecutando la sentencia UPDATE
            # --------------------------    
            # cursor.execute(sentencia_update, valor_update)               # Actualizar 1 solo registro
            cursor.executemany(sentencia_update, valores_update)         # Actualizar varios registros
            
            # Obtener el número de registros insertados
            registros_modificados = cursor.rowcount

            print(f'[INFO] Registros Modificados: {registros_modificados}\n')
except Exception as e:
    print(f'[ERROR] Ocurrio un error inespeado: {e}\n')
finally:
    print(f'[INFO] Conexión finalizada...\n')