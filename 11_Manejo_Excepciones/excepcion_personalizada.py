# --------------------------
# Creación de una Excepción Personalizada
# --------------------------
class NumerosIgualesError(Exception):
    
    # Personalizamos el mensaje de error
    def __init__(self, mensaje):
        self.message = mensaje
