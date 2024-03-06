
class ManejoArchivos:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def __enter__(self):
        print('Obteniendo Recursos'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerrando Recursos'.center(50,'-'))
        
        # Si el atributo nombre esta apuntando a un objeto tipo archivo, lo cerrara
        if self.nombre:
            self.nombre.close()