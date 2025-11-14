# 📂 Uso de Base de Datos con PostgreSQL (pgAdmin)

---

## 📌 1. Creación de Base de Datos en PostgreSQL

### 🔹 Paso 1: Crear una nueva Base de Datos
1. Abrir **pgAdmin**
2. Expandir el panel izquierdo: `Servers > PostgreSQL > Databases`
3. Click derecho en **Databases** y selecciona **Crear**
4. Configuración:

    4.1 Nombre de la db: `test_db`

    4.2 Propietario: `postgres`

### 🔹 Paso 2: Crear una tabla `persona` dentro de la db
1. Expandir el panel izquierdo: `test_db > Schemas > public > Tables`
2. Click derecho en **Tables** y seleccionar: `Create > Table`
3. Configuración:

    3.1 Nombre: `persona`
    
    3.2 Propietario: `postgres`

4. Seleccionar pestaña `Columns`
5. Agregar las siguientes columnas:

| Nombre     | Tipo de Dato                     | Restricciones         |
| ---------- | -------------------------------- | --------------------- |
| id_persona | SERIAL                           | Primary Key, Not Null |
| nombre     | VARCHAR(50) [character varying]  | —                     |
| apellido   | VARCHAR(50) [character varying]  | —                     |
| email      | VARCHAR(100) [character varying] | —                     |

### 🔹 Paso 3: Insertar datos en la tabla `persona`
1. Agregar información a la tabla:

    1.1 Click derecho en tabla `persona`

    1.2 Seleccionar `View/Edit Data > All Rows`

    1.3 En la seccion inferior donde muestra la tabla vacia, rellenar los campos: **nombre**, **apellido**, **email** (No se considera **id_personas** porque asigna automaticamente el número)

    1.4 Posteriormente guardar los datos registrados

### 🔹 Paso 4: Consultar los registros agregados
1. Realizar la siguiente consulta SQL

```sql
SELECT * FROM persona
```

---

## 📌 2. Ejecución básica de consultas SQL

### 🔹 Obtener todos los registros de la tabla `persona`
```sql
SELECT * FROM persona;
```

Resultado: 

- Muestra todas las **columnas** y **filas** de la tabla.

### 🔹 Mostrar sólo un registro específico de la tabla `persona`
```sql
SELECT * 
FROM persona
WHERE id_persona = 1;
```
Donde:

- **WHERE id_persona = 1** devuelve únicamente la fila con este valor.

### 🔹 Mostrar 2 o más registros específico de la tabla `persona`
```sql
SELECT *
FROM persona
WHERE id_persona IN (1,2);
```
Donde:

- **WHERE id_persona IN (1, 2)** devuelve múltiples filas cuyos `id_persona` estén en la tabla.

### 🔹 Insertar un nuevo registro
```sql
INSERT INTO persona(nombre, apellido, email)
VALUES ('Pepito', 'Gonzalez', 'pgonzalez@email.cl')
```
Donde:

- **INSERT INTO** permite agregar una nueva fila en la tabla.

### 🔹 Actualizar un registro existente
```sql
UPDATE persona
SET nombre = 'Perez', email = 'pperez@email.co'
WHERE id_persona = 3;
```
Donde:

- **UPDATE** permite modificar valores existentes donde **SET** permite asignar los nuevos valores al registro ingresando el nombre de la columna
- **WHERE** indica qué registro se actualizada, es decir, la persona con **id_persona = 3**

### 🔹 Eliminar un registro existente
```sql
DELETE FROM persona
WHERE id_persona = 3;
```
Donde:

- **DELETE** elimina el registro de la tabla
- **IMPORTANTE:** Si se omite la sentencia **WHERE**, se borrarán **todos los registros**

### 🔹 Comentar líneas en SQL
```sql
-- SELECT * FROM persona WHERE id_persona = 2;
```
