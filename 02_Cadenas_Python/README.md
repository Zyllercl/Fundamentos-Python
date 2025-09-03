# 📂 Cadenas en Python

---

## 📌 1. Cadenas
> **Definición:**
> - Una **cadena** o *string* es un tipo de dato que almacena una secuencia de caracteres.
> - En Python, las cadenas se encierran entre **comillas dobles** (`" "`) o **comillas simples** (`' '`).
> - Los caracteres pueden ser letras, números, símbolos o espacios.

**Ejemplo:**
```python
texto_1 = "Hola Mundo"
texto_2 = 'Python es lo mejor'
```

### 📌 1.1 Detalles de un String
> - Los caracteres de una cadena están **indexados** de manera secuencial.
> - Esto permite acceder a cada caracter indicando su **índice** (posición).
> - Los índices comienzan en `0` y pueden ser **negativos** (`-1` es el último caracter)

| Operación     | Resultado      |
|---------------|----------------|
| **string[0]**     | `Primer caracter` |
| **string[-1]**    | `Último caracter` |
| **string[0:5]**   | `Caracteres de íncide 0 al 4` |

**Ejemplo:**
```python
frase = "Obteniendo un caracter"

print(frase[0])     # 'O' -> primer caracter
print(frase[-1])    # 'r' -> último caracter
print(frase[0:5])   # 'Obten -> caracteres del índice 0 al 4
```

### 📌 1.2 Inmutabilidad de un String
> **Definición:**
> - En Python, las cadenas son **inmutables**, no se pueden modificar sus caracteres directamente.
> - Si se quiere cambiar, hay que **crear una nueva cadena**.

**Ejemplo:**
```python
frase = "Hola Mundo"
frase[0] = "h" # ❌ Error: 'str' object does not support item assignment
```

---

## 📌 2. Caracteres especiales en Strings
> **Definición:**
> - Las cadenas apueden incluir **caracteres especiales**. Estos caracteres se introducen usando la **diagonal inventida** (`\`).

**Ejemplo:**

| Caracter | Descripción | Ejemplo en Python | Resultado |
|--------------|-----------------|----------------------|---------------|
| `\n`         | Salto de línea  | `"Hola\nMundo"`       | Hola<br>Mundo |
| `\t`         | Tabulación      | `"Hola\tMundo"`       | Hola Mundo |
| `\'`         | Comilla simple  | `'It\'s ok'`          | It's ok |
| `\"`         | Comilla doble   | `"Ella dijo: \"Hola\""` | Ella dijo: "Hola" |
| `\\`         | Barra invertida | `"C:\\Users\\Pepe"`   | C:\Users\Pepe |

---

## 📌 3. Concatenación de Strings
> **Definición:**
> - La concatenación de strings permite combinar dos o más para formar una nueva cadena.

**Ejemplo:**

| Método         |                Descripción                                                | Ejemplo en Python                       | Resultado             |
|----------------|---------------------------------------------------------------------------|-----------------------------------------|-----------------------|
| `+`            | Concatenación directa de dos strings                                      | `"Hola" + " Mundo"`                     | Hola Mundo            | 
| `join()`       | Une varias cadenas usando un separador, se debe pasar una lista de string | `", ".join(["Python", "es", "genial"])` | Python, es, genial    |

---

## 📌 4. Formateo de Strings
> **Definición:**
> - Python incliue varias maneras de concatenar cadenas, insertar variables e incluso dar otro tipo de formateo.

**Ejemplo:**

| Método        | Descripción                                           | Ejemplo en Python                     | Resultado     |
|---------------|-------------------------------------------------------|---------------------------------------|---------------|
| f-string      | Inserta variables directamente dentro de la cadena    | `nombre = "Pepe"; f"Hola {nombre}"`    | Hola Pepe      |
| format()      | Usa `{}` como placeholders y reemplaza con valores    | `"Hola {}".format("Pepito")`             | Hola Pepito      |

---

## 📌 5. Métodos de Strings
> **Definición:**
> - Los strings en Python incluyen métodos útiles que facilitan su manipulación

**Ejemplo:**

| Método        | Descripción                                          | Ejemplo en Python              | Resultado              |
|---------------|------------------------------------------------------|--------------------------------|------------------------|
| `upper()`     | Convierte la cadena a mayúsculas                     | `"hola".upper()`               | HOLA                   |
| `lower()`     | Convierte la cadena a minúsculas                     | `"HOLA".lower()`               | hola                   |
| `strip()`     | Elimina espacios al inicio y al final                | `"  hola  ".strip()`           | hola                   |
| `len()`       | Devuelve la longitud de la cadena                    | `len("Hola Mundo")`            | 10                     |

---

## 📌 6. Subcadenas en Strings
> **Definición:**
> - Una subcadena es una parte de un string principal.
> - Se pueden extraer subcadenas, buscarlas, reemplazarlas, entre otras operaciones.

| Método                   | Descripción                                                                             | Ejemplo en Python                     | Resultado                |
|--------------------------|-----------------------------------------------------------------------------------------|---------------------------------------|--------------------------|
| Slicing (`[inicio:fin]`) | Extrae parte de la cadena usando índices (sin incluir el último carácter)               | `"Hola Mundo"[0:4]`                   | Hola                     |
| find()                   | Devuelve el índice de la pripera aparición de la subcadena (si no encuentra la subcadena, devuelve -1) | `"Hola Mundo".find("Mundo")` | 5                  |
| replace()                | Reemplaza una subcadena por otra dentro del string ṕrincipal                            | `"Hola Mundo".replace("Mundo","Python")` | Hola Python           |
| split()                  | Divide una cadena en una lista de subcadenas basadas en un carácter separador           | `"Hola,Mundo,Python".split(",")`      | ['Hola', 'Mundo', 'Python'] |

