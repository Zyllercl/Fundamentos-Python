
# Lectura de archivo
archivo = open('prueba.txt', 'r') # R -> Solo lectura
""" print(archivo.read()) """

# Leer algunos caracteres
""" print(archivo.read(5))
print(archivo.read(3)) """

# Leer lineas completas
""" print(archivo.readline())
print(archivo.readline()) """

# Iterarcion de un archivo
""" for linea in archivo:
    print(linea) """

# Leer todas las lineas de un archivo (LISTA)
""" print(archivo.readlines()) """

# Leer una linea de la lista del archivo
""" print(archivo.readlines()[0]) """

# Crear una copia de un archivo
# a -> Anexar Informacion (se traspasa la informacion sin sobreescribir el archivo nuevo)
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()

print('Se ha copiado el archivo correctamente')