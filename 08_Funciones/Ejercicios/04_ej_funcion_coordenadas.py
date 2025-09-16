print(f'[EJEMPLO] Obtener Coordenadas X - Y - Z\n')

# -----------------------------
# Definición de la función
# -----------------------------
def coordenadas():
    # Variables Locales
    x, y, z = 10, 20, 30

    # Retorno de Varias Variables
    return x, y, z

# -----------------------------
# Llamada a la función
# # -----------------------------
resultado = coordenadas()

print(f'Tupla de Valores: {resultado}\n') # Retornará una tupla de valores

# -----------------------------
# Unpacking de la Tupla
# -----------------------------
x1, y1, z1 = resultado

print(f'Coordenada X = {x1} \nCoordenada Y = {y1} \nCoordenada Z = {z1}')