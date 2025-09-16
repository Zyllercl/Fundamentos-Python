"""
Función con Argumentos por nombre
=================================

Definición:
-----------

Cuando se declara una función con argumentos, se pueden asignar valores por defecto. 

Sintaxis:

    def mi_funcion(argumento_1 = None, argumento_2 = None)
        # Bloque de código....
"""

print(f'[FUNCION CON ARGUMENTOS]\n')

# ---------------------
# Definición de funcion con argumentos
# ---------------------
def persona(nombre, apellido, edad):
    print(f'Persona: Nombre = {nombre} ; Apellido = {apellido} ; Edad = {edad}')

# ---------------------
# Llamada a la función con argumentos
# ---------------------
print(f'Función con argumentos')
persona('Sansa', 'Stark', 28) # Los argumentos ingresados deben ser de manera posicional, es decir, como fueron declarados en la función.

# ---------------------
# Llamada a la función usando los argumentos por nombre
# ---------------------
print(f'\nFunción con argumentos por nombre')
persona(nombre='Jon', apellido='Snow', edad=38)

# ---------------------
# Llamada a la función usando los argumentos por nombre, pero de forma desordenada
# ---------------------
print(f'\nFunción con argumentos por nombre (desordenado)')
persona(apellido='Stark', edad=50, nombre='Ned')

# ---------------------
# Llamada a la función con valores por default
# ---------------------
def persona2(nombre, apellido='', edad=0):
    print(f'\nPersona: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}')

persona2(nombre='Daenarys')