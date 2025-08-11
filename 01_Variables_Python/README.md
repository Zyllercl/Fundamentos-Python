# 📂 Variables en Python

---

## 📌 1. Variables
> **Definición:**
> Una **variable** es un nombre que almacena un valor en la **memoria RAM**.
> En Python, las variables son **dinámicas**: pueden guardar distintos tipos de datos (textos, números, booleanos, listas, etc.) sin declarar el tipo previamente.

### 🔹 Reglas básicas
- No pueden comenzar con un número.
- No usar **palabras reservadas** (`for`, `if`, `class`, `try`, etc.).
- Python es **case-sensitive**: `mi_nombre` y `Mi_nombre` son variables diferentes.

### 🔹 Tipos de variables
| Estilo        | Ejemplo         | Uso común              |
|---------------|----------------|------------------------|
| camelCase     | `mensajeNuevo` | Programación en Java   |
| PascalCase    | `MensajeNuevo` | Nombres de clases      |
| flat case     | `nombrenuevo`  | Poco común             |
| kebab-case    | `nombre-nuevo` | ❌ No válido en Python  |
| snake_case ✅ | `nombre_nuevo` | Convención recomendada |

---

## 📌 2. Tipos de Datos
> **Definición:**
> Python es un lenguaje de **tipado dinámico**: no necesitas especificar el tipo de dato al declarar la variable.
> La variable puede cambiar de tipo durante la ejecución del programa.

### 🔹 Tipos de datos más comunes
| Tipo     | Descripción                 | Ejemplo          |
|----------|-----------------------------|------------------|
| `str`    | Cadena de texto              | `"Hola mundo"`   |
| `int`    | Número entero                | `42`             |
| `float`  | Número decimal               | `3.14`           |
| `bool`   | Valor lógico                  | `True`, `False`  |
| `None`   | Ausencia de valor             | `None`           |

### 🔹 Diferencia de Tipados
| Tipo                  | Descripción | Ejemplo |
|-----------------------|-------------|---------|
| **Tipado Estático**   | Se declara el tipo de dato y la variable solo puede almacenar valores de ese tipo. | `int edad = 20`  *(solo números enteros)* |
| **Tipado Dinámico**   | La variable puede contener cualquier tipo de dato y reasignarse a valores de distinto tipo. | `edad = 20`<br>`edad = "Python"` |

---

## 📌 3. Constantes
> **Definición:**
> Python **NO** tiene constantes "reales", pero por **convención** se escriben en **mayúsculas** para indicar que no deberían cambiar.

