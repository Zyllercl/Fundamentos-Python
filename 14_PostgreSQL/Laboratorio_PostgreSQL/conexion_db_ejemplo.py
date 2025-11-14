"""
Para ejecutar este archivo se necesita activar el entorno virtual, previamente se debe haber instalado el paquete psycopg2.

Comandos para activar el entorno virtual e instalar psycopg2:
    - Linux:
        source .env/bin/activate
    
    - Windows:
        .\venv\Scripts\activate

Ejecutar archivo:
    python3 conexion_db_ejemplo.py
"""

# Importando el módulo psycopg2 para conectarse a PostgreSQL
import psycopg2

with psycopg2.connect(
    # Estableciendo la conexión a la base de datos PostgreSQL
    user="postgres", password="postgres",
    host="localhost", port="5432", database="test_db"
) as conexion:
    print(f'\n[INFO] Conexión exitosa...\n')

    # Creación de un cursor para ejecutar comandos SQL
    with conexion.cursor() as cursor:
        # --------------------------
        # Párametro para la sentencia SQL
        # --------------------------
        # id_persona = input("Proporciona el id_persona a buscar: ")
        # llaves_primarias = ((1,2),)     # Tupla de tuplas para la cláusula IN
        entrada = input('Porporciona los ID\'s a buscar (separados por coma): ')
        print()
        llaves_primarias = (tuple(entrada.split(',')),) # Tupla de tuplas para la cláusula IN de manera dinámica
        
        # --------------------------
        # Setencias SQL
        # --------------------------
        # sentencia_fetchall = "SELECT * FROM persona"
        # sentencia_fetchone = "SELECT * FROM persona WHERE id_persona = %s"
        sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
        
        # --------------------------
        # Ejecutando las sentencias SQL
        # --------------------------
        # cursor.execute(sentencia_fetchall)                  # Sentencia SQL para buscar todos los registros
        # cursor.execute(sentencia_fetchone, (id_persona,))   # Sentencia SQL para buscar 1 registro en específico
        cursor.execute(sentencia, llaves_primarias)           # Sentencia SQL para buscar varios registros en específico
        
        # --------------------------
        # Obteniendo los registros
        # --------------------------
        # registros = cursor.fetchall()       # fetchall devuelve todos los registros
        # registro = cursor.fetchone()        # fetchone devuelve un solo registro
        registros = cursor.fetchall()       # fetchall devuelve varios registros

        # --------------------------
        # Confirmar cambios en la base de datos
        # --------------------------
        # conexion.commit() -> No es necesario usarlo con el manejador de contexto 'with' porque lo hace automáticamente.

        for registro in registros:
            # Mostrando los registros obtenidos
            print(registro)

    # Cerrando la conexión
    print(f'\n[INFO] Conexión finalizada...\n')