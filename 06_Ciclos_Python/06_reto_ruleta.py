'''
    ADIVINA EL NUMERO

    Def:
        - Crear un juego donde el jugador debe adivinar un número secreto. puedes usar un ciclo while hasta que el jugador adivine correctamente. 
        - El número secreto se puede crear usando la funcion randint para generar un valor aleatorio entre 1 y 30
        - Por cada intento fallido se debe incrementar una variable que llegue el conteo de intentos
        - El programa debe indicar al jugador si el número ingresado fue mayor o menor que el número secreto
        - Finalmente si adivina el número secreto debe felicitar al usuario e indicar cuantos intentos realizó
        - Opcionalmente, puedes limitar e juego a un numero de intentos máximo 
'''

from random import randint

print(f'-----   ADIVINA EL NUMERO PREMIADO  -----')
# Variables
NUM_MIMINO = 1
NUM_MAXIMO = 20
INTENTOS_MAX = 5

intentos = 0
numero_secreto = randint(NUM_MIMINO,NUM_MAXIMO)
numero_usuario = None

while numero_usuario != numero_secreto and intentos < INTENTOS_MAX:
    numero_usuario = int(input(f'Ingresa un número entre {NUM_MIMINO} y {NUM_MAXIMO}: '))    

    if numero_usuario < numero_secreto:
        print(f'El número secreto es mayor!')
    elif numero_usuario > numero_secreto:
        print(f'El número secreto es menor!')
    
    # Incremento intentos
    intentos += 1

if numero_usuario == numero_secreto:
    print(f'¡Felicidades! Adivinaste el número secreto en {intentos} intentos.')
else:
    print(f'Has agotado tus intentos: {intentos}')
    print(f'El numero secreto era: {numero_secreto}')