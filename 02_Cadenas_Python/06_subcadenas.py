"""
Uso de Subcadenas en Strings en Python
======================================
Este script muestra cómo trabajar con subcadenas de un string principal, usando métodos como `find`, `replace`, `split`, `slicing` y la multiplicación de cadenas.
Se incluyen ejemplos prácticos de extracción, búsqueda, reemplazo y división de cadenas, así como un ejercicio didáctico para normalizar un nombre y crear un correo electrónico.
"""

# -------------------------------------
# Extracción de subcadenas (Slicing)
# -------------------------------------
variable_original = 'Hola, Mundo!\n'

subcadena_hola = variable_original[0:4]
subcadena_mundo = variable_original[6:11]

print(f'Variable Original: {variable_original}')
print(f'Subcadena "Hola": {subcadena_hola}')
print(f'Subcadena "Mundo": {subcadena_mundo}\n')

# -------------------------------------
# Buscar subcadenas con find()
# -------------------------------------
indice_subcadena_mundo = variable_original.find('Mundo')
print(f'Índice de la subcadena "Mundo" es: {indice_subcadena_mundo}')

indice_subcadena_hola = variable_original.find('hola')
print(f'Índice de la subcadena "hola" es: {indice_subcadena_hola}\n') # Devuelve -1 porque 'hola' no se encuentra en la variable original (Case Sensitive)

# -------------------------------------
# Reemplazar subcadenas con replace()
# -------------------------------------
reemplazar_subcadena = variable_original.replace('Mundo', 'Adios')
print(f'Reemplazo de subcadena: {reemplazar_subcadena}')

# -------------------------------------
# Dividir un string con split()
# -------------------------------------
ejemplo_1 = 'Hola Mundo'
lista_1 = ejemplo_1.split()   # Por defecto separa por espacios en blanco
print(f'Ejemplo 1: {ejemplo_1}')
print(f'Separación en subcadenas (Default): {lista_1}\n')

ejemplo_2 = 'Pepe,10,Alexandria'
lista_2 = ejemplo_2.split(',')    # Separación en subcadenas como delimitador la coma
print(f'String Original: {ejemplo_2}')
print(f'Separación en subcadenas con coma: {lista_2}\n')

# -------------------------------------
# Multiplicación de strings
# -------------------------------------
texto = 'Hola'
veces = 3
resultado = texto * veces
print(f'Multiplicación de cadenas: {resultado}\n')


# -------------------------------------
# Ejercicio didáctico: Normalización de texto para correo
# -------------------------------------
nombre_completo = " Pepe Perez   "
nombre_normalizado = nombre_completo.strip()                # Elimina espacios en blanco al inicio y al final de un string
nombre_normalizado = nombre_normalizado.replace(' ', '.')   # Reemplaza los espacios por un punto
nombre_normalizado = nombre_normalizado.lower()             # Conversion a minusculas

nombre_empresa = "  empresa de ejemplo  "
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower() # Elimina espacios en blanco y convierte todo a minusculas

extension_dominio = ".cl"
dominio_correo_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'

print(f'Correo electronico generado: {nombre_normalizado}{dominio_correo_normalizado}')

