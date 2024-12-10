'''
    SUBCADENAS EN STRINGS

    Def:
        - Una subcadena es una parte de un string principal. Se puede extraer subcadenas, buscarlas, reemplazarlas, entre otras operaciones.
            Ejemplos:
                - Extracción de cadenas (Slicing)               # El Slicing (segmentación) permite indicar el índice de inicio y el índice final (sin incluir este último caracter).

                - Buscar Subcadenas (find)                      # El método find() devuelve el índice de la priemra aparición de la subcadena. Si no encuentra la subcadena, devuelve un -1.

                - Reemplazar Subcadenas (replace)               # El método replace() permite reemplazar una subcadena por otra dentro de una cadena principal.

                - Extraer subcadenas por separadores (split)    # El método split() permite dividir una cadena en una lista de subcadenas basadas en un caracter sepador.

'''

'''     USO DE SUBCADENAS EN STRINGS    '''
# Extracción de cadenas
variable_original = 'Hola, Mundo!\n'

subcadena_hola = variable_original[0:4]
subcadena_mundo = variable_original[6:11]
print(f'Variable Original: {variable_original}')
print(f'Subcadena_hola: {subcadena_hola}')
print(f'Subcadena_mundo: {subcadena_mundo}\n')

'''     USO DE SUBCADENAS METODO FIND    '''
# Buscar Subcadenas (Método find)
indice_subcadena_mundo = variable_original.find('Mundo')
print(f'El índice de la subcadena Mundo es: {indice_subcadena_mundo}')
indice_subcadena_hola = variable_original.find('hola')
print(f'El índice de la subcadena hola es: {indice_subcadena_hola}\n') # Devuelve -1 porque 'hola' no se encuentra en la variable cadena_original (Case Sensitive)

'''     USO DE SUBCADENAS METODO REPLACE    '''
# Reemplazar Subcadenas (Método replace)
reemplazar_subcadena = variable_original.replace('Mundo', 'Adios')
print(f'Reemplazo de subcadena: {reemplazar_subcadena}')

'''     USO DE SUBCADENAS METODO SPLIT    '''
# Dividir un String
datos = 'Hola Mundo'
print(f'String Original: {datos}')
lista = datos.split()   # Por defecto separa cada elemento por espacios en blanco}
print(f'Separacion en subcadenas (Default): {lista}\n')

datos = 'Daereys,33,Islandia'
print(f'String Original: {datos}')
lista = datos.split(',')    # Separación en subcadenas como delimitador la coma
print(f'Separacion en subcadenas: {lista}\n')

# Multiplicación de cadenas
texto = 'Hola'
veces = 3
resultado = texto * veces
print(f'Multiplicacion de cadenas: {resultado}\n')

# Ejercicio Didactico
nombre_completo = " Bellamy Blake  "
nombre_normalizado = nombre_completo.strip() # Elimina espacios en blanco al inicio y al final de un string
nombre_normalizado = nombre_normalizado.replace(' ', '.') # Reemplaza los espacios por un punto
nombre_normalizado = nombre_normalizado.lower() # Conversion a minusculas

nombre_empresa = "  The 100  "
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower() # Elimina esacios en blanco y convierte todo a minusculas

extension_dominio = ".cl"
dominio_correo_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'

print(f'Correo electronico: {nombre_normalizado}{dominio_correo_normalizado}')

