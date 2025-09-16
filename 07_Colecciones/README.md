# 📂 Colecciones en Python

---

## 📌 1. Colecciones (Listas - Tuplas - Sets - Diccionarios)
> **Definición:**
> - Una **colección** es un conjunto de datos.
> - En Python existen varios tipos de colecciones que nos permiten **almacenar, organizar y manipular** múltiples conjuntos de datos, esto se conoce como `Estructura de Datos`.

### 🔹 Tipos de Estructuras de Datos

| **Tipo**       | **Descripción** |
|----------------|-----------------|
| **Lista**      | Colección **ordenada y mutable** de elementos. Puede cambiar de tamaño, añadir - modificar y eliminar elementos, y puede contener distintos tipos de datos. |
| **Tupla**      | Colección **ordenada e inmutable**. Una vez creada, no se puede modificar ni su tamaño ni sus elementos. |
| **Set**        | Colección **no ordenada** de elementos **únicos**. No admite duplicados y permite agregar/eliminar elementos, pero no modificarlos. |
| **Diccionario**| Colección **ordenada** que almacena datos en pares **llave:valor**. Se accede a los elementos mediante su índice, es decir, la "llave" para acceder al "valor". |

### 🔹 Ejemplos de Estructuras de Datos

| **Tipo**       | **Ejemplo de Sintaxis** |
|----------------|--------------------------|
| **Lista**      | `lista = [elemento1, elemento2, elemento3]` |
| **Tupla**      | `tupla = (elemento1, elemento2, elemento3)` <br> `tupla_sin_parentesis = elemento1, elemento2, elemento3` |
| **Set**        | `conjunto = {elemento1, elemento2, elemento3}` |
| **Diccionario**| `diccionario = {llave1: valor1, llave2: valor2}` |

## 📌 2. List Comprehension
> **Definición:**
> - Las `List Comprehension` es una forma concisa y eficiente de crear **listas** a partir de otros iterables (listas, tuplas, set o diccionarios).
> - Permite filtrar elementos y aplicar expresiones a cada elemento de un iterable, es decir, se puede **crear una iteración dentro de una lista** para simplificar la declaraciones de nuevos valores.

### 🔹 Sintaxis Comprensión de Listas

```python
# Sintaxis de una List Comprehension
list_comprehension = [nueva_expresion for elemento in iterable if condicion]
```
**Donde:**

| **Componente**   | **Descripción**   |
|------------------|-------------------|
| nueva_expresion  | Es la expresión que define cómo se modifica o procesa cada elemento del iretable |
| elemento         | Variable que representa a cada elemento del iterable original                    |
| iterable         | Secuencia o colección sobre la cual se va a iterar                               |
| condicion        | [Opcional] Es una condición para filtrar los elementos del iretable              |