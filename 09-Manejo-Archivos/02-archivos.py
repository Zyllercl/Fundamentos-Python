

def app():
    # Abrir un archivo y se cierra automaticamente
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            # rstrip() elimina el salto de linea
            print(contenido.rstrip())

app()