'''
    FUNCION RANGE: STRING

    Def: Uso de la funcion 'range' para iterar strings
        - 
                        
'''

print(f'-----   FUNCION RANGE: STRING   -----')
# Variables
mensaje = input('Escrime un mensaje a repetir: ')
repeticiones = int(input('Ingresa el número de repeticiones: '))

# Iterar sobre un rango de repeticiones
for i in range(repeticiones):
    # Cabe destacar que i inicia en 0 y la cantidad de repeticiones va a ser: repeticiones - 1 (en terminos de posicionamiento)
    print(f'Iteracion[{i}]: {mensaje}')