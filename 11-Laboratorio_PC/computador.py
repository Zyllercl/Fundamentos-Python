from teclado import Teclado
from mouse import Mouse
from monitor import Monitor


class Computador:
    # Variables Globales
    contador_computadores = 0
    
    # Metodos
    def __init__(self, nombre, monitor, teclado, mouse):
        # Aumentamos el contador
        Computador.contador_computadores += 1
        # Atributos
        self._id_computador = Computador.contador_computadores # Seteamos la ID con el contador
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse
        
    def __str__(self) -> str:
        return f'''
            {self._nombre}: {self._id_computador}
            Monitor: {self._monitor}
            Teclado: {self._teclado}
            Mouse: {self._mouse}
        '''
        
if __name__ == '__main__':
    print('[!] Testeando clase Computador...')
    
    # Creacion de los objetos Teclado | Mouse | Monitor para la Computadora1
    teclado1 = Teclado('HP', 'USB')
    mouse1 = Mouse('HP', 'USB')
    monitor1 = Monitor('HP', 20)
    
    computador1 = Computador('Basico', monitor1, teclado1, mouse1)
    print(computador1)
    
    # Creacion de los objetos Teclado | Mouse | Monitor para la Computadora2
    teclado2 = Teclado('Redragon', 'Bluetooth')
    mouse2 = Mouse('Logitech', 'Bluetooth')
    monitor2 = Monitor('Samsung', 24)
    
    computador2 = Computador('Gamer', monitor2, teclado2, mouse2)
    print(computador2)