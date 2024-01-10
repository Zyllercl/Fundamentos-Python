
# Funciones que retornen un Valor

# Funciones
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