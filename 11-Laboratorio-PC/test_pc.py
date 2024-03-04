from teclado import Teclado
from mouse import Mouse
from monitor import Monitor
from computador import Computador
from orden import Orden


print('[!] Testeando aplicacion completa...')

# Objetos
teclado1 = Teclado('HP', 'USB')
mouse1 = Mouse('HP', 'USB')
monitor1 = Monitor('HP', 20)
computador1 = Computador('Basico', monitor1, teclado1, mouse1)

# Objetos
teclado2 = Teclado('Redragon', 'Bluetooth')
mouse2 = Mouse('Logitech', 'Bluetooth')
monitor2 = Monitor('Samsung', 24)
computador2 = Computador('Gamer', monitor2, teclado2, mouse2)

# Objetos
teclado3 = Teclado('Gamer', 'Bluetooth')
mouse3= Teclado('Gamer', 'Bluetooth')
monitor3 = Monitor('Zowie', 27)
computador3 = Computador('Gamer', monitor3, teclado3, mouse3)

# Lista de objetos de tipo computadora
computadores1 = [computador1, computador2]
# Inicializacion de una nueva orden
orden1 = Orden(computadores1)
# print(orden1)
orden1.agregar_computador(computador3)
print(orden1)

computadores2 = [computador2, computador3]
orden2 = Orden(computadores2)
print(orden2)