'''
    VARIABLES EN PYTHON

    Def:
        - Una variable en Python es un nombre que almacena un valor guardado en la memoria temporal del PC. 
        - Las variables en Python son dinámicas, es decir, que pueden almacenar cualquier tipo de valores como por ejemplo: Texto, números enteros, decimales, booleanos, listas, etc.

    Variables y la Memoria RAM:     
        - En Python, cada vez que se crea una variable y le asignamos un valor, estamos reservando espacio en memoria RAM.
        - Las variables no pueden comenzar con números, no se pueden usar palabras reservadas (Keyword) como por ej: for, if, class, try, etc.
        - Python es case sensitive, es decir, que hace la diferencia entre variables declaradas con mayúsculas y minusculas por ej: 'mi_nombre' es diferente a 'Mi_nombre'

    Tipos de declaración de Variables:
        - mensajeNuevo    -> camelCase
        - MensajeNuevo    -> Pascal Case
        - nombrenuevo     -> Falt Case
        - nombre-nuevo    -> Kebab Case
        - nombre_nuevo    -> Snake Case [*] 'Es recomendable usar esta opcion en terminos de convención y buenas practicas'
'''

'''     USO DE VARIABLES    '''
# Sintaxis para definir una variable
nombre_de_la_variable = 'valor'

# Obtener la pocision de memoria de una variable
print('Posición de Memoria:', id(nombre_de_la_variable))

# Declaración de variables y asignación de valores
nombre = "Lord Stark"   # Variable tipo Texto
edad = 40               # Variable tipo Entero
peso = 70.4             # Variable tipo Float
es_casado = True        # Variable tipo Boolean

# Acceder a las variables
print('\nValores Originales')
print('Nombre:', nombre)
print('Edad:', edad)
print('Peso:', peso)
print('Casado:', es_casado)

# Modificar el valor de una variable
nombre = "Daerys Targaryen"
edad = 30

# Acceder a las variables
print('\nValores Modificadas')
print('Nombre:', nombre)
print('Edad:', edad)

'''     REGLAS Y CONVENCIONES    '''
# Reglas y Convenciones en nombres de variables
print('\nReglas y Convenciones')
nombre_usuario = "Usuario 1"
# 1nombre_usuario = "Usuario 1" <- [ERROR] No se puede crear una variable con un numero al principio.
# class = "Usuario"             <- [ERROR] No se puede crear una variable con un nombre reservado (class).

# Case Sensitive
nombre = "Usuario 1"
Nombre = "Usuario 2"

print('La variable "nombre" es:', nombre, ', es diferente de "Nombre":', Nombre)

# Prefijos y Subfijos
es_casado = False           # Corresponde a un prefijo, es decir, 'es_xxxx' hace alusion a una variable Booleana
nombre_txt = "archivo.txt"  # Corresponde a un subfijo, es decir, xxxx_txt hace alusion a una variable que guarda un archivo tipo 'txt'

