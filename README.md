
# Crear un entorno virtual con python
> Entrar a la carpeta seleccionada
* python -m venv .venv
> Activar entorno Virtual
* cd .venv\Scripts
* activate
> Actualizar entorno Virtual
* python -m pip install --upgrade pi

### Configuracion para instalar Postgresql en entorno virtual
> Instalacion de Psycopg2
* python -m pip install psycopg2-binary

### Configuracion de postgresql para psycog2 [Modulo 15-DB_postgesql]

- Entrar a la ruta de postgresql al archivo: postgresql.conf y agregar al final lo siguiente
* lc_messages = 'en-US'
* lc_monetary = 'en-US'
* lc_numeric = 'en-US'
* lc_time = 'en-US'