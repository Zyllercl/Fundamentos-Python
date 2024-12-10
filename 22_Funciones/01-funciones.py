
# Funciones

"""
    Que es una función? -> Bloque de código diseñado para realizar una actividad
                        -> Las funciones pueden ser reutilizadas
"""

# Definir una funcion
def informacion():
    print('Hola Mundo!')

informacion()

# Funciones que retornen un Valor
def informacion(nombre):
    return nombre

# Variables
empleado = informacion('Elmo')
print(empleado)

# Entregar multiples parametros, se conoce como *args
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Pedro', 'Juan', 'Diego')