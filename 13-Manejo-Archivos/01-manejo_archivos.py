
# Creacion y escribir datos en un archivo

def app():
    try:
        # Crear un archivo
        archivo = open('prueba.txt', 'w', encoding='utf8' ) # W -> Escritura
        archivo.write('Agregamos lineas al archivo \n')
        archivo.write('Siguiente linea...')
    except Exception as e:
        print(e)
    finally:
        archivo.close()
        
    """ # Generar numeros en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea: ' + str(i) + "\n") """
    
app()