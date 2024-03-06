
class Orden:
    # Variables Globales
    contador_ordenes = 0
    
    def __init__(self, computadores):
        # Aumentamos el contador
        Orden.contador_ordenes += 1
        # Atributos
        self._id_orden = Orden.contador_ordenes # Seteamos la ID con el contador
        self._computadores = computadores
        
    def agregar_computador(self, computador):
        # Atributos
        self._computadores.append(computador) # Agregando un nuevo objeto al listado de computadores
        
    def __str__(self) -> str:
        # Variables
        computadores_str = ''
        
        for computador in self._computadores:
            computadores_str += computador.__str__()
        
        return f'''
                Orden: {self._id_orden}
                Computadoras: {computadores_str}
        '''