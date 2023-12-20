
# Creacion y escribir datos en un archivo


def app():
    # Crear un archivo
    archivo = open('archivo.txt', 'w') # W -> Escritura

    # Generar numeros en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea: ' + str(i) + "\n")
    
    # Cerrar el archivo
    archivo.close()

app()