# 📂 Operadores en Python

---

## 📌 1. Operadores
> **Definición:**
> - Los operadores son símbolos especiales que están diseñados para realizar operaciones específicas como:

| Categoría                   | Descripción                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Operadores Aritméticos      | Realizan cálculos matemáticos básicos (suma, resta, multiplicación, división). |
| Operadores de Asignación    | Asignan valores a una variable.                                             |
| Operadores de Comparación   | Comparan un valor con otro.                                                 |
| Operadores Lógicos          | Combinan expresiones o condiciones lógicas.                                 |
| Operadores de Identidad     | Verifican si dos variables son el mismo objeto.                             |
| Operadores de Membresía     | Comprueban si un elemento está presente en una secuencia (ej. subcadena).   |

---

## 📌 2. Operadores Aritméticos
> **Definición:**
> - Los operadores aritméticos permiten realizar cálculos matemáticos básicos entre números.

| Operador | Nombre             | Descripción                                                       |
|----------|--------------------|-------------------------------------------------------------------|
| `+`      | Suma               | Suma de dos operandos.                                            |
| `-`      | Resta              | Resta de dos operandos.                                           |
| `*`      | Multiplicación     | Multiplica dos operandos.                                         |
| `/`      | División           | Divide el primer operando entre el segundo (resultado flotante).  |
| `//`     | División Entera    | Divide el primer operando entre el segundo (resultado entero).    |
| `%`      | Módulo             | Retorna el residuo de una división.                               |
| `**`     | Exponente          | Eleva el primer operando a la potencia del segundo.               |

---

## 📌 3. Operadores de Asignación
>**Definición:**
> - Los **operadores de asignación** se utilizan para asignar un valor a una variable mediante el carácter `=`.
> - En Python existen dos variantes útiles:
> 1. **Asignación Múltiple:** Permite asignar valores a varias variables en una sola línea de código, lo que hace que el código sea más compacto y legible.
> 2. **Asignación Encadenada:** Permite asignar el mismo valor a múltiples variables.

| Tipo de Asignación     | Sintaxis                                        | Ejemplo en Python      |
|------------------------|-------------------------------------------------|------------------------|
| Asignación simple      | `variable = valor`                              | `x = 10`               |
| Asignación múltiple    | `variable1, variable2 = valor1, valor2`         | `a, b = 5, 8`          |
| Asignación encadenada  | `variable1 = variable2 = ... = valor`           | `m = n = p = 100`      |

---

## 📌 4. Operadores de Asignación Compuestos
> **Definición:**
> - Los operadores de asignación compuestos combinan una operación aritmética (o bit a bit) con la asignación en una sola expresión.
> - En lugar de escribir la operación y luego asignar el resultado a la misma variable, se hace en un sólo paso.

| Operador | Equivale a... | Descripción |
|----------|---------------|-------------|
| `+=`     | `a = a + b`   | Suma el valor de `b` a `a` y asigna el resultado a `a`. |
| `-=`     | `a = a - b`   | Resta el valor de `b` a `a` y asigna el resultado a `a`. |
| `*=`     | `a = a * b`   | Multiplica `a` por `b` y asigna el resultado a `a`. |
| `/=`     | `a = a / b`   | Divide `a` entre `b` (resultado flotante) y lo asigna a `a`. |

---

## 📌 5. Operadores Condicionales
> **Definición:**
> - Los **operadores condicionales** se utilizan para comparar dos valores.
> - El resultado siempre es un valor booleano (`True` o `False`), dependiendo de si la condición se cumpple o no.

| Operador | Nombre     | Descripción | Ejemplo |
|----------|------------|-------------|---------|
| `==`     | Igualdad   | Compara si dos valores son iguales | `a == b` |
| `!=`     | Distinto   | Compara si dos valores son distintos | `a != b` |
| `<`      | Menor que  | Verifica si el valor de la izquierda es menor que el de la derecha | `a < b` |
| `<=`     | Menor o igual que | Verifica si el valor de la izquierda es menor o igual que el de la derecha | `a <= b` |
| `>`      | Mayor que         | Verifica si el valor de la izquierda es mayor que el de la derecha | `a > b` |
| `>=`     | Mayor o igual que | Verifica si el valor de la izquierda es mayor o igual que el de la derecha | `a >= b` |

---

## 📌 6. Operadores Lógicos
> **Definición:**
> - Los **operadores lógicos** se utilizan para realizar operaciones lógicas con valores booleanos.

**Operador Lógico AND**
> Devuelve `True` sí ambos operandos son **verdaderos**

| a      | b      | a and b |
|--------|--------|---------|
| False  | False  | False   |
| False  | True   | False   |
| True   | False  | False   |
| True   | True   | True    |

**Operador Lógico OR**
> Devuelve `True` si cualquiera de los operando es **verdadero**

| a      | b      | a or b |
|--------|--------|--------|
| False  | False  | False  |
| False  | True   | True   |
| True   | False  | True   |
| True   | True   | True   |

**Operador Lógico NOT**
> Invierte el valor del operando.

| a      | not a  |
|--------|--------|
| False  | True   |
| True   | False  |

```python
Sintáxis Operador NOT:
valor = False
print(not valor) -> TRUE
```
---

## 📌 7. Precedencia de Operadores
> **Definición:**
> - La **precedencia de operadores** determina el orden en que se evalúan las operaciones en una expresión.
> - Python aplica la siguiente tabla para asegurar que algunos operadores tengan mayor propiedad que otros durante la evaluación de expresiones:

| Operador                       | Descripción                                      |
|--------------------------------|--------------------------------------------------|
| ()                             | Paréntesis: fuerza la prioridad de evaluación    |
| **                             | Exponente                                        |
| +x, -x                         | Operadores unarios (positivo y negativo)         |
| *, /, //, %                    | Multiplicación, División, División entera, Módulo|
| +, -                           | Suma y resta                                     |
| ==, !=, <, <=, >, >=           | Comparación                                      |
| not, and, or                   | Operadores lógicos                               |
| =, +=, -=, /=, //=, **=        | Operadores de asignación    
