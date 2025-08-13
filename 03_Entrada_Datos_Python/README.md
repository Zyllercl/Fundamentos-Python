# 📂 Entrada de Datos en Python

---

## 📌 1. Conversión de Tipos de Datos (Casting)
> **Definición:**
> - La conversión de tipos de datos, conocida como `casting`, sirve para manipular y cambiar su tipo de dato.
> - Se puede realizar conversiones **desde y hacia distintos tipos de datos**

**Ejemplo:**

| Función     | Descripción                           | Ejemplo en Python          | Resultado  |
|-------------|---------------------------------------|----------------------------|------------|
| `int()`     | Convierte a número entero             | `int(3.7)`                 | 3          |
| `float()`   | Convierte a número flotante           | `float(5)`                 | 5.0        |
| `str()`     | Convierte a cadena de texto           | `str(100)`                 | '100'      |
| `bool()`    | Convierte a booleano                  | `bool(0)`                  | False      |
| `bool()`    | Convierte a booleano                  | `bool(5)`                  | True       |

---

## 📌 2. Entrada de Datos por Consola
> **Definición:**
> - La entrada de datos se realiza utilizando la función `input()`
> - Esta función pausa el programa y espera a que el usuario introduzca algpun texto desde el teclado
> - Los datos ingresados por consola son tratados cono **Strings (str)**

### 🔹 Características
> - **Interactividad:** Permite a los usuarios proporcionar valores dinámicos.
> - **Secillez:** Se debe especificar un mensaje claro indicando lo que se solicita al usuario.
> - **Tipo de dato:** Todo dato ingresado por consola se maneja como cadena **(string)**.

---

## 📌 3. Generar Números Aleatorios
> **Definición:**
> - La función `randint()` forma parte del módulo **random**, que permite generar números aleatorios.
> - Para usar esta función, primero se debe importar el módulo. Existen dos formas:
> 1. `import random`: Importa todos los métodos y funciones del módulo **random**.
> 2. `from random import randint`: Importa únicamente la función **randint()**.

**Ejemplo:**
| Función / Método    | Descripción                                                           | Ejemplo en Python    | Resultado Ejemplo   |
|---------------------|-----------------------------------------------------------------------|----------------------|---------------------|
| `randint(a, b)`     | Devuelve un número entero aleatorio entre `a` y `b`, incluyendo ambos | `randint(1, 10)`     | 7 (ejemplo)         |