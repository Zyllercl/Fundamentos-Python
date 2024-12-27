print(f'-----   OBTENER COORDENADAS X Y Z   -----')

# Definicion de la funcion
def coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z

# Llamada a la funcion
resultado = coordenadas()
print(f'{resultado}') # Retornará una tupla de valores

# Unpacking de la Tupla
x1, y1, z1 = resultado
print(f'Coordenada x1 = {x1} \nCoordenada y2 = {y1} \nCoordenada z1 = {z1}')