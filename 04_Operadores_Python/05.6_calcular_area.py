'''
    CALCULAR AREA Y PERIMETRO DE UN RECTANGULO

    Def:
        - Crear un programa que solicite al usuario ingresar dos valores (base y altura) para calcular el área y perímetro de un rectángulo.

            Formulas:
                - area = base * altura
                - perimetro 2 * (base + altura)
'''

print(f'-----   CALCULAR AREA Y PERIMETRO DE UN RECTANGULO   -----')
# Variables
base = int(input('Ingresa la base: '))
altura = int(input('Ingrese la altura: '))

area = base * altura
perimetro = 2 * (base + altura)

print(f'''\n
DATOS:
Base: {base}
Altura: {altura}

RESULTADOS:
Área: {area}
Perimetro: {perimetro}
''')