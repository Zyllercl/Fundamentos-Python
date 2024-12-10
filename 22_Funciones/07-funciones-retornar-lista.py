
# Devolver una lista
def devolver_lista(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Pedro', 'Juan', 'Diego']
devolver_lista(nombres)

# No se puede puede entregar un valor INT ya que debe ser iterable por el FOR
# devolver_lista(10) # ERROR
# Para resolver esto se deben agregar los valores en forma de TUPLA
devolver_lista((10, 20, 30))
# Tambien se puede devolver en formato de LISTA
devolver_lista([30, 20, 10])