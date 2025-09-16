"""
RETO: Adivina el número

Definición:
-----------

Crear un programa donde el jugador debe adivinar un número secreto. Puedes usar un ciclo while hasta que el jugador adivine correctamente. El programa debe indicar al jugador si el número ingresado fue mayor o menor que el número secreto. Opcionalmente, puedes limitar el juego a un número de intentos máximo.

Tener en consideración lo siguiente:
    1. El número secreto se puede crear usando la función randint para generar un valor aleatorio entre 1 y 30.
    2. Por cada intento fallido se debe incrementar una variable que lleve el conteo de intentos.
"""

from random import randint

print(f'[RETO] Adivina el número')
# Variables Constantes
NUM_MIMINO = 1
NUM_MAXIMO = 20
INTENTOS_MAX = 5

intentos = 0
numero_secreto = randint(NUM_MIMINO,NUM_MAXIMO)
numero_usuario = None

# ------------------
# Ciclo principal del juego
# ------------------
while numero_usuario != numero_secreto and intentos < INTENTOS_MAX:
    # Ingreso de datos: Número
    numero_usuario = int(input(f'Ingresa un número entre {NUM_MIMINO} y {NUM_MAXIMO}: '))    

    # Validación del número ingresado
    if numero_usuario < numero_secreto:
        print(f'El número secreto es mayor!')
    elif numero_usuario > numero_secreto:
        print(f'El número secreto es menor!')
    
    # Incremento intentos
    intentos += 1

# Comprueba si el usuario adivinó el número
if numero_usuario == numero_secreto:
    print(f'¡Felicidades! Adivinaste el número secreto en {intentos} intentos.')
else:
    print(f'\nHas agotado tus intentos: {intentos}')
    print(f'El numero secreto era: {numero_secreto}')