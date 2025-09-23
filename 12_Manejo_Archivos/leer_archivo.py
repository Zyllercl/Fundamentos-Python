
# --------------------------------
# Manejo de Archivos - Lectura
# --------------------------------
archivo = open('test.txt', 'r', encoding='utf-8')

# --------------------------------
# Leer algunos caracteres del archivo (Descomentar print para ver el resultado)
# --------------------------------

# Lee los primeros 4 caracteres
# print(f'[LECTURA] Primeros 6 carácteres: {archivo.read(6)}') 

# Lee los siguientes 11 caracteres
# print(f'[LECTURA] Siguientes 11 carácteres: {archivo.read(11)}\n')

# --------------------------------
# Leer línea por línea (Descomentar print para ver el resultado)
# --------------------------------
# print(f'[LECTURA - LINEA] Primera línea (vacía): {archivo.readline()}') # Muestra vacío porque ya se leyeron los primeros caracteres
# print(f'[LECTURA - LINEA] Segunda línea: {archivo.readline()}')

# --------------------------------
# Iterar sobre las líneas del archivo
# --------------------------------
# for linea in archivo:
#     print(f'[ITERACION] {linea}', end='') # El end='' es para evitar doble salto de línea

# --------------------------------
# Leer todo el contenido del archivo
# --------------------------------
# print('\n[INFO] Contenido del archivo:\n')
# print(archivo.read())

# --------------------------------
# Leer todas las líneas y devolverlas en una lista
# --------------------------------
# print(archivo.readlines())

# --------------------------------
# Leer una línea específica de la lista
# --------------------------------
# print(archivo.readlines()[1]) # Lee la segunda línea (índice 1)

# --------------------------------
# Abrir un nuevo archivo traspasando información del archivo anterior
# --------------------------------
nuevo_archivo = open('copia_test.txt', 'a', encoding='utf-8')
nuevo_archivo.write(archivo.read())

archivo.close()
nuevo_archivo.close()
print('\n[INFO] Trasferencia de datos completada y archivos cerrados.')