# 📂 Módulo de Funciones en Python

---

## 📌 1. Definición de Funciones
> **Definición:**
> - Las funciones en Python son bloques de código para realizar una tarea en particular.
> - Se pueden reutilizar en diferentes partes de un programa.
> - Para mandar a llamar una función, primero se debe declarar; si se hace a la inversa, dará un error de función no declarada.

### 🔹 Ventajas de las Funciones
1. **Modularidad:** Permite dividir un programa en partes más pequeñas y manejables. Cada función puede ser desarrollada por separado e incluso por distintos programadores.
2. **Reutilización de código:** Una vez creada la función, se puede utilizar tantas veces como sea necesario, evitando duplicación de código y minimizando errores.
3. **Mantenimiento:** Modificar un programa que usa funciones es más fácil; los errores se localizan más rápido y se corrigen reduciendo riesgos en otras partes del programa.
4. **Parametrización:** Las funciones pueden aceptar parámetros, haciendo los programas más flexibles.
5. **Colaboración:** En proyectos grandes, el uso de módulos (archivos con múltiples funciones) es imprescindible para colaborar con varios programadores.

**Ejemplo: Funciones sin y con argumentos**

| Tipo de Función      | Descripción                               | Ejemplo en Python                         | Resultado       |
|---------------------|-------------------------------------------|------------------------------------------|----------------|
| Sin argumentos      | Función que no recibe parámetros          | `def saludar(): print("Hola")`           | `Hola`         |
| Con argumentos      | Función que recibe parámetros             | `def sumar(a, b): return a + b`          | `sumar(3,5)` → 8 |

---

## 📌 2. Argumentos Variables (`*args`)
> **Definición:**
> - Permiten que una función acepte un número arbitrario de argumentos posicionales.
> - Se reciben como una **tupla** dentro de la función.
> - La entrega de parámetros a `*args` es opcional.

**Ejemplo:**
```python
def suma(*args):
    total = 0
    for num in args:
        total += num
    return total

suma(1,2,3,4)  # Resultado: 10
```

---

## 📌 3. Argumentos Variables (`**kargs`)
> **Definición:**
> - Permiten que una función acepte un número arbitrario de argumentos con llave-valor.
> - Se reciben como un diccionario dentro de la función.
> - La entrega de parámetros a `**kwargs` es opcional.

**Ejemplo:**
```python
def mostrar_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mostrar_info(nombre="Pepe", edad=17)
# Resultado:
# nombre: Pepe
# edad: 17

```

---

## 📌 4. Alcance de Variables
> **Definición:**
> - Las variables pueden tener **alcance global** o **local** dependiendo de dónde y cuándo se declaren.

| Tipo de Variable     | Definición                                  | Ejemplo en Python                          |
|---------------------|--------------------------------------------|-------------------------------------------|
| Global              | Disponible en todo el programa             | `x = 10` fuera de cualquier función       |
| Local               | Disponible solo dentro del bloque o función| `def f(): y = 5`                          |

---

## 📌 5. Módulos en Python
> **Definición:**
> - Un módulo es un archivo que puede contener la definición de variables o funciones.
> - Ejemplo: Carpeta `ejemplo_modulo` con los archivos:
>   - `modulo_funcion_sumar.py`: Contiene la función `sumar()`
>   - `sumar.py`: Archivo desde el cual se importa y llama la función `sumar()` del módulo anterior


---

## 📌 6. Funciones Recursivas
> **Definición:**
> - Una **función recursiva** es aquella que se llama **a sí misma** y debe acercarse a un caso base para evitar ciclos infinitos.

**Ejemplo:**
```python
def cuenta_regresiva(n):
    if n == 0:   # Caso base (punto de parada)
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n-1)  # Se llama a sí misma con un número más pequeño

cuenta_regresiva(5)

# Resultado:
5
4
3
2
1
¡Despegue!
```