
# Excepcion de Numeros Identicos

class NumerosIdenticos(Exception):
    
    # Definicion de las clases de excepcion
    def __init__(self, mensaje):
        self.message = mensaje