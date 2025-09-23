# 📂 Manejo de Excepciones en Python

---

## 📌 1. Excepciones en Python
> **Definición:**
> - Las **excepciones** son eventos que ocurren durante la ejecución de un programa y que interrumpen su flujo normal.
> - En Python, las excepciones se manejan utilizando las palabras clave:

| Palabra Clave | Descripción                                                         |
| ------------- | ------------------------------------------------------------------- |
| `try`         | Bloque donde se ejecuta el código que puede producir una excepción. |
| `except`      | Bloque que captura y maneja la excepción.                           |
| `else`        | Bloque que se ejecuta si no ocurre ninguna excepción.               |
| `finally`     | Bloque que se ejecuta siempre, ocurra o no una excepción.           |


### Nota Importante
- Se pueden encadenar múltiples bloques `except`, cada uno para un tipo específico de excepción.
- El **orden es importante**: primero se deben colocar las excepciones más específicas y después las más generales, para evitar que una excepción general capture a todas las demás.

## 📌 2. Tipos de Excepciones
| Excepción           | Descripción                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| `Exception`         | Clase base para todas las excepciones integradas, excepto las de salida del sistema.              |
| `ZeroDivisionError` | Ocurre cuando se intenta dividir un número por cero.                                              |
| `ValueError`        | Se produce cuando una función recibe un argumento con el tipo correcto pero un valor inapropiado. |
| `TypeError`         | Aparece cuando se aplica una operación o función a un objeto de tipo incorrecto.                  |
| `IndexError`        | Sucede cuando se accede a un índice fuera del rango válido de una lista o tupla.                  |
| `KeyError`          | Ocurre al intentar acceder a una clave inexistente en un diccionario.                             |
| `FileNotFoundError` | Se lanza cuando se intenta abrir un archivo que no existe.                                        |

## 📌 3. Estructura Básica de Excepciones
```python
try:
    # Código que puede generar una excepción
except TipoDeExcepcion:
    # Código para manejar la excepción
else:
    # Código que se ejecuta si no hubo excepción
finally:
    # Código que se ejecuta siempre, haya o no excepción
```
