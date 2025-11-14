# 📂 PostgreSQL en Python

---

## Crear un entorno virtual con python
1. Dirigirse a la carpeta **Laboratorio_PostgreSQL** e ingresar el siguiente comando

```bash
python3 -m venv .env
```
Esto generará un entorno virtual.

2. Activar entorno virtual

```bash
source .env/bin/activate
```

3. Desactivar entorno virtual
```bash
deactivate
```

4. Actualizar entorno Virtual
```bash
python3 -m pip install --upgrade pip
```

## Instalación de Psycopg (Paquete de PostgreSQL en Python)
```bash
python -m pip install psycopg2
python -m pip install psycopg2-binary
python -m pip install psycopg-pool (opcional)
```

---

## Conexión a la Base de Datos con Python 
Revisar archivo: `conexion_db_ejemplo.py`