from computador import Computador

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
        Orden.contador_ordenes +=1

        # ----------------------
        # Atributos de Instancia
        # ----------------------
        self.id_orden = Orden.contador_ordenes
        self.computadores = computadores
    
    def __str__(self):
        mensaje = ''

        for computador in self.computadores:
            mensaje += '\n' + computador.__str__()
        
        return f'''N° ORDEN: {self.id_orden}
        Computador: {mensaje}
        '''
    
    # ----------------------
    # Métodos
    # ----------------------
    def agregar_computador(self, computador):
        # Agregar PC a la lista
        self.computadores.append(computador)