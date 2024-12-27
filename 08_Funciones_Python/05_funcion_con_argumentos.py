'''
    FUNCION CON ARGUMENTOS POR NOMBRE

    -   Cuando se declara una funcion con argumentos, se puede asignar valores por defecto de la siguiente forma:

        def mi_funcion(argumento1=None, argumento2=None):
            # Bloque de código
'''

print(f'-----   FUNCION CON ARGUMENTOS   -----')

def persona(nombre, apellido, edad):
    print(f'Persona: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}')

# Llamada a la función pasando los argumentos de manera posicional, es decir, como fueron declarados en la función (ordenado)
persona('Sansa', 'Stark', 28)

# Llamada a la función usando los argumentos por nombre
persona(nombre='Jon', apellido='Snow', edad=38)

# Llamada a la función usando los argumentos por nombre, pero de forma desordenada
persona(apellido='Stark', edad=50, nombre='Eddard')

# Llamada a la función con valores por default
def persona2(nombre, apellido='', edad=0):
    print(f'Persona: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}')

persona2(nombre='Daenarys')