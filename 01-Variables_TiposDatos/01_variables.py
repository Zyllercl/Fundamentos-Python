'''
    Variables en Python

    Def:    Una variable en Python es un nombre que almacena un valor guardado en la memoria temporal del PC.
            Las variables en Python son dinámicas, es decir, que pueden almacenar cualquier tipo de valores como por ejemplo: Texto, números enteros, decimales, booleanos, listas, etc.

    Variables y la Memoria RAM:    En python, cada vez que se crea una variable y le asignamos un valor, estamos reservando espacio en memoria RAM.

    Tipos de Variables:
                        mensajeNuevo    -> camelCase
                        MensajeNuevo    -> Pascal Case
                        nombrenuevo     -> Falt Case
                        nombre-nuevo    -> Kebab Case
                        nombre_nuevo    -> Snake Case [*]
'''

# Sintaxis para definir una variable
nombre_de_la_variable = valor

# Obtener la pocision de memoria de una variable
print(id(nombre_de_la_variable))

# Declaración de variables y asignación de valores
nombre = "Lord Stakes"   # Variable tipo Texto
edad = 40                # Variable tipo entero
peso = 70.4              # Variable tipo float
es_casado = True         # Variable tipo boolean

# Acceder a las variables
print('Nombre:', nombre)
print('Edad:', edad)
print('Peso:', peso)
print('Casado:', es_casado)


