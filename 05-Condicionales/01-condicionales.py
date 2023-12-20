
# Condicionales en Python

"""
    Operadores Condicionales

    ==  -> Igual a
    !=  -> Diferente a
    >   -> Mayor a
    >=  -> Mayor o igual a
    <   -> Menor a
    <=  -> Menor o igual a

"""

# Condicional 'Mayor a'
monto = 100

if monto > 99:
    print('Tienes dinero')
else:
    print('No tienes dinero')

# Condicional 'Mayor o igual a'
likes = 200

if likes >= 200:
    print('Excelente, tienes muchos likes')

# Condicional con texto
lenguaje = 'Python'

if lenguaje == 'python':
    print('Las palabras son iguales')
else:
    print('Python es Case Sensitive')

# Condicional con Booleanos
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso permitido')
else:
    print('Acceso denegado!')