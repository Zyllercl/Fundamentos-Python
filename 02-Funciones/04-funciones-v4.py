
# Funciones y Metodos

# Variables
nombre = 'Elmo'

# Funciones
def mostrar_nombre(nombre):
    print(f'Hola {nombre}')

mostrar_nombre(nombre)

# Diferentes metodos en Python
print(nombre.upper()) # Metodo para hacer todo en mayuscula
print(nombre.title()) # Metodo para hacer la primera en mayuscula

# Reto

# Funcion que imprime un mensaje
def mensaje_bienvenida():
    print('Bienvenido a Python')

mensaje_bienvenida()

# Funcion que tome un nombre y lo muestre como mensaje
nombre = 'elmo'

def bienvenido(nombre):
    print(f'Bienvenido terricola {nombre}')

bienvenido(nombre)

# Funcion que retorne otra funcion
def llamando_bienvenido():
    bienvenido('Miguel')

llamando_bienvenido()
