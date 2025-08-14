'''
    SISTEMA DE CALIFICACIONES

    Def:
        - Crear un programa para determinar el costo de un envio de un paquete según sea el destino (nacional o internacional) y el peso del paquete.
            COSTO TARIFAS:
            - Nacional = 10.000 x kilo
            - Internacional = 20.000 x kilo
        
        - El programa debe solicitar 2 valores:
            1.- Destino (nacional o internacional)
            2.- Peso (Kg) del paquete
'''

print(f'-----   SISTEMA DE CALIFICACIONES   -----')
# Variables
TARIFA_NACIONAL = 10000
TARIFA_INTERNACIONAL = 20000

destino_paquete = input('Cual es el destino del paquete? (Nacional/Internacional): ')
peso_paquete = int(input('Cuanto pesa el paquete (kg)?: '))
costo_envio = None

if destino_paquete.strip().lower() == 'nacional':
    costo_envio = peso_paquete * TARIFA_NACIONAL
elif destino_paquete.strip().lower() == 'internacional':
    costo_envio = peso_paquete * TARIFA_INTERNACIONAL
else:
    print(f'No existe el tipo de envio {destino_paquete}')

if costo_envio is not None:
    print(f'El costo de envío del paquete es de: ${costo_envio}')