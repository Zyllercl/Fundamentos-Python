from teclado import Teclado
from monitor import Monitor
from mouse import Mouse

# ----------------------
# Creación de Clase
# ----------------------
class Computador():
    # ----------------------
    # Atributos de Clases
    # ----------------------
    contador_computadores = 0

    # ----------------------
    # Constructor
    # ----------------------
    def __init__(self, nombre, monitor, teclado, mouse):
        # Aumento del contador
        Computador.contador_computadores += 1

        # ----------------------
        # Atributos de Instancia
        # ----------------------
        self.id_monitor = Computador.contador_computadores
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.mouse = mouse

    # Modificación del Método STR
    def __str__(self):
        mensaje = f'''{self.nombre} : {self.id_monitor}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Mouse: {self.mouse}\n'''

        return mensaje

# ----------------------
# Pruebas
# ----------------------
if __name__ == '__main__':
    # Creación de los Objetos de tipo Computador (Gama Media)
    teclado = Teclado('Redragon', 'USB')
    mouse = Mouse('Logitech', 'USB')
    monitor = Monitor('Samsung', 24)
    computador_1 = Computador('PC Gama Media', monitor, teclado, mouse)

    print(computador_1)

    # Creación de los Objetos de tipo Computador (Gama Alta)
    teclado = Teclado('Logitech', 'Wireless')
    mouse = Mouse('Logitech', 'Wireless')
    monitor = Monitor('MSI', 27)
    computador_2 = Computador('PC Gama Alta', monitor, teclado, mouse)

    print(computador_2)

