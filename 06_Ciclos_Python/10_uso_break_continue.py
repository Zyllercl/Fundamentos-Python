'''
    USO DE BREAK Y CONTINUE EN CICLO FOR

    Def:
        - Uso de BREAK:     La palabra reservada 'break' permite finalizar un ciclo for

        - Uso de CONTINUE:  La palabra reservada 'continue' permite continuar el programa saltandose sin tomar en cuenta el valor actual
                        
'''

print(f'-----   CICLO FOR: USO DE BREAK   -----')
# Uso de break
for numero in range(1, 10):
    # Obtener el primer numero par y terminar el ciclo
    if numero % 2 == 0:
        print(numero)
        break

print(f'\n-----   CICLO FOR: USO DE BREAK   -----')
# Uso de break
for numero in range(1, 10):
    # Condicion: Todo numero impar entra al 'continue', es decir, que no lo tomara en cuenta (no lo imprimira por consola) y seguira con la siguiente iteracion
    if numero % 2 == 1:
        continue
    
    # Se mostraran sólo los numeros pares
    print(numero)