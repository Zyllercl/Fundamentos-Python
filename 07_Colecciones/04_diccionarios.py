"""
Uso de Diccionarios en Python
=============================

Definición:
-----------

Los Diccionarios en Python son estructuras de datos que almacenan pares de llave-valor. Permiten un acceso rápido a los valores mediante sus llaves asociadas.

Características principales:
 
    1. Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación.
    2. Las llaves deben ser únicas y de un tipo inmutable (como cadenas, números o tuplas).
    3. Los valores pueden ser de cualquier tipo de dato, incluyendo otros diccionarios.
    4. Los diccionarios no mantienen un orden específico de los elementos (hasta Python 3.6, donde se mantiene el orden de inserción).

Operaciones comunes:

    - Acceso a elementos: Se accede a los valores mediante sus llaves.
    - Agregar o modificar elementos: Se pueden agregar nuevos pares llave-valor o modificar los existentes.
    - Eliminar elementos: Se pueden eliminar pares llave-valor utilizando la palabra clave `del` o el método `pop()`.
    - Iterar sobre elementos: Se puede iterar sobre las llaves, valores o ambos utilizando métodos como `.keys()`, `.values()` y `.items()`.
    - Métodos útiles: Algunos métodos comunes incluyen `.get()`, `.update()`, `.clear()`, entre otros.

*IMPORTANTE*: Los diccionarios son muy útiles para almacenar y gestionar datos estructurados, como configuraciones, registros y cualquier otra información que requiera una asociación clara entre llaves y valores.
"""

print(f'[DICCIONARIOS EN PYTHON]')

# ---------------------
# Ejemplo de un diccionario
# ---------------------
persona = {
    'nombre': 'Pepe',
    'edad': 25,
    'es_mayor': True
}

print(f'Ejemplo de un Diccionario: {persona}\n')

# ---------------------
# Acceso a los elementos del diccionario, ya sea por su llave o usando el método .get()
# ---------------------
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}')
print(f'Edad: {persona.get("es_mayor")}\n')

# ---------------------
# Agregar y Modificar elementos del diccionario
# ---------------------

# Agregar un nuevo elemento al diccionario
persona['ciudad'] = 'Santiago'

print(f'Agregar un elemento al Diccionario (ciudad): {persona}\n')

# Modificar un valor del diccionario
persona['edad'] = 28
print(f'Modificar un valor de un Diccionario (edad): {persona}\n')

# ----------------------
# Eliminar un elemento del diccionario, ya sea usando 'del' o el método .pop()
# ----------------------

# Forma 1: Método del
del persona['edad']
print(f'Eliminacion de un elemento del Diccionario (edad): {persona}\n')

# Forma 2: Método pop()
persona.pop('ciudad')
print(f'Diccionario persona: {persona}\n')
