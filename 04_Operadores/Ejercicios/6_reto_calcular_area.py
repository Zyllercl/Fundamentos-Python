"""
RETO: Calcular área y perímetro de un rectángulo
================================================

Definición:
-----------

Crear un programa que solicite al usuario ingresar dos valores (base y altura) para calcular el área y perímetro de un rectángulo.

Formulas:
- área = base * altura
- perímetro = 2 * (base + altura)
"""

# ---------------------------
# Ejemplo de uso del operador de multiplicación y suma
# ---------------------------
print(f'[RETO: CALCULAR ÁREA Y PERÍMETRO DE UN RECTÁNGULO]\n')

# ---------------------------
# Entrada de datos
# ---------------------------
base = int(input('Ingresa la base: '))
altura = int(input('Ingrese la altura: '))

# ---------------------------
# Cálculo del área y perímetro
# ---------------------------
area = base * altura
perimetro = 2 * (base + altura)

print(f'''\n
Resultados:
Área del rectángulo: {area}
Perimetro del rectángulo: {perimetro}
''')