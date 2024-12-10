
# Devolver un objeto (lista) por funcion **kwargs
def listar_objetos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave} : {valor}')

listar_objetos(PK='Primary Key', Name='Mopa', Age='30')