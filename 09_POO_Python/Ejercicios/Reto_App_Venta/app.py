# ----------------------
# Laboratorio App Venta
# ----------------------
from monitor import Monitor
from teclado import Teclado
from mouse import Mouse
from computador import Computador
from orden import Orden

print(f'\n[APP VENTA PC]\n')

# ----------------------
# PC 1: Gama Media
# ----------------------
monitor_1 = Monitor('Samsung', 24)
teclado_1 = Teclado('Redragon', 'Wireless')
mouse_1 = Mouse('Redragon', 'USB')
computador_1 = Computador('Gama Media', monitor_1, teclado_1, mouse_1) 
# print(computador_1)

# ----------------------
# PC 2: Gama Alta
# ----------------------
monitor_2 = Monitor('MSI', 27)
teclado_2 = Teclado('Logitech', 'Wireless')
mouse_2 = Mouse('Logitech', 'Wireless')
computador_2 = Computador('Gama Alta', monitor_2, teclado_2, mouse_2)
# print(computador_2)

# ----------------------
# Creación Lista de Computadores
# ----------------------
computadores = [computador_1, computador_2]
orden_1 = Orden(computadores)

# ----------------------
# Agregar un PC a la lista
# ----------------------
monitor_3 = Monitor('LG', 21)
teclado_3 = Teclado('Razer', 'USB')
mouse_3 = Mouse('Razer', 'USB')
computador_3 = Computador('Gama Media-Alta', monitor_3, teclado_3, mouse_3)
orden_1.agregar_computador(computador_3)    # Uso del método creado en Orden.py
print(orden_1)
