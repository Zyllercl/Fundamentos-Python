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

# Declaración de variables y asignación de valores
nombre = "Lord Stakes"   # Variable tipo Texto
edad = 40                # Variable tipo entero
peso = 70.4              # Variable tipo float
es_casado = True         # Variable tipo boolean


mensaje_nuevo = 'Hola Mundo'
print(mensaje_nuevo)

# Retos
omam = 'Mountain Sound'
print(omam)


# Obtener la pocision de memoria de una variable
print(id(mensaje_nuevo))
print(id(omam))
