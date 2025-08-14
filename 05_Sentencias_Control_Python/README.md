# 📂 Sentencia de Control

---

## 📌 1. Sentencias de decisión
> **Definición:**
> - Las **sentencias de decisión** permiten controlar el flujo de ejecución de un programa.
> - Existen diferentes tipos de sentencias de decisión:

| Sentencia        | Descripción                                                               |
|------------------|---------------------------------------------------------------------------|
| if               | Ejecuta un bloque de código solo si la condición es verdadera (True)      | 
| if else          | Permite ejecutar un bloque si la condición es falsa (False)               |
| if elif else     | Permite evaluar múltiples condiciones secuenciales                        |

**Ejemplo:**
| Sentencia        | Sintaxis / Ejemplo                                                                              |
|------------------|-------------------------------------------------------------------------------------------------|
| if               | if condicion: → Bloque de código que se ejecuta si la condición es `True`                       |
| if else          | if condicion: → Bloque `True` ; else: → Bloque `False`                                          |
| if elif else     | if condicion1: → Bloque condición1 `True` ; elif condicion2: → Bloque condición2 `True` ; else: → Bloque `False` |

---

## 📌 2. Operador Ternario
> **Definición:**
> - Un **operador ternario** en Python es una forma compacta de agregar una condición.
> - El objetivo es asignar un valor a una variable dependiendo del valor de la condición.

| Caso               | Operación / Resultado                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------|
| Sintaxis           | resultado = valor_si_verdadero if condicion else valor_si_falso                                  |
| Asignación Simple  | edad = 20 → resultado = "Mayor de edad" if edad >= 18 else "Menor de edad"                       |
| Explicación        | Evalúa la condición `edad >= 18`; si es True asigna "Mayor de edad", si es False "Menor de edad" |