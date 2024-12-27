'''
    FUNCION QUE REGRESA VARIOS VALORES
'''

print(f'-----   FUNCION QUE RETORNA VARIOS VALORES   -----')

# Definicion de la funcion
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta función retornará varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

# Programa principal
nombre, apellido, edad = persona_mayusculas('sansa', 'stark', 28)

print(f'Resultado: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}')