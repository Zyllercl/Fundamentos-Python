"""
RETO: Sistema de Envíos
=======================

Definición:
-----------

Crear un programa para determinar el costo de un envío de un paquete según sea el destino (nacional o internacional) y el peso del paquete. Considerar lo siguiente:

    1. Si el destino es nacional, el costo es de 10.000 por kilo.
    2. Si el destino es internacional, el costo es de 20.000 por kilo.

El programa debe solicitar 2 valores:

    1. Destino (nacional o internacional)
    2. Peso (Kg) del paquete
"""

print(f'[SISTEMA DE ENVÍOS]\n')

# -----------------------------
# Variables de tarifas
# -----------------------------
TARIFA_NACIONAL = 10000
TARIFA_INTERNACIONAL = 20000

# -----------------------------
# Solicitar datos al usuario
# -----------------------------
destino_paquete = input('Cual es el destino del paquete? (Nacional/Internacional): ')
peso_paquete = int(input('Cuanto pesa el paquete (kg)?: '))
costo_envio = None

# -----------------------------
# Calcular el costo de envío según el destino
# -----------------------------
if destino_paquete.strip().lower() == 'nacional':
    costo_envio = peso_paquete * TARIFA_NACIONAL
elif destino_paquete.strip().lower() == 'internacional':
    costo_envio = peso_paquete * TARIFA_INTERNACIONAL
else:
    print(f'No existe el tipo de envio {destino_paquete}')

# -----------------------------
# Imprimir el costo de envío si se ha calculado
# -----------------------------
if costo_envio is not None:
    print(f'El costo de envío del paquete es de: ${costo_envio}')