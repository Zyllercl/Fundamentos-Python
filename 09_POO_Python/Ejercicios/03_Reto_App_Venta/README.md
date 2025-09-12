# Ejercicio de POO Aplicando Herencia, Polimorfismo y Clase Object

Crear un programa de venta de computadores, para ello se debe ocupar todo lo visto hasta este punto, es decir, definición de clases, métodos, herencia, polimorfismo y clase object.

- **El archivo `app.py` contiene la estructura para crear una Orden de Compra**
---

## Crear las siguientes clases

1. Dispositivo Entrada:
    - Parámetros:
        - marca
        - tipo_entrada

2. Raton:
    - Parámetros:
        - contador_ratones
        - id_raton
    - Métodos:
        - `__init__ ()`
        - `__str__ ()`

3. Teclado:
    - Parámetros:
        - contador_teclados
        - id_teclado
    - Métodos:
        - `__init__ ()`
        - `__str__ ()`

4. Monitor:
    - Parámetros:
        - contador_monitores
        - id_monitor
        - marca
        - tamaño
    - Métodos:
        - `__init__ ()`
        - `__str__ ()`

5. Computador:
    - Parámetros:
        - contador_computadores
        - id_computador
        - nombre
        - monitor : Monitor
        - teclado : Teclado
        - raton   : Raton
    - Métodos:
        - `__init__ ()`
        - `__str__ ()`

6. Orden:
    - Parámetros:
        - contador_ordenes
        - id_ordenes
        - computadores : list
    - Métodos:
        - `agregar_computador()`
        - `__init__ ()`
        - `__str__ ()`