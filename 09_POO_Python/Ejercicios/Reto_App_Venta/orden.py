from computador import Computador
from teclado import Teclado
from monitor import Monitor
from mouse import Mouse

# ----------------------
# Creación de Clase
# ----------------------
class Orden(Computador):
    # ----------------------
    # Atributos de Clase
    # ----------------------
    contador_ordenes = 0

    # ----------------------
    # Constructor
    # ----------------------
    def __init__(self, computadores):
        # Aumento del contador
        self.id_orden = Orden.contador_ordenes
        # ----------------------
        # Atributos de Instancia
        # ----------------------
        self.computadores = computadores
    
    def __str__(self):
        mensaje = ''

        for computador in self.computadores:
            mensaje += '\n' + computador.__str__()
        
        f'''ORDEN N°: {self.id_orden}
        Computador: {mensaje}
        '''
    
    # ----------------------
    # Métodos
    # ----------------------
    def agregar_computador(self, computador):
        # Agregar PC a la lista
        self.computadores.append(computador)