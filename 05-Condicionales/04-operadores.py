
# Operadores

"""
    Operador AND    -> Se deben cumplir todas condiciones
    Operador OR     -> Se debe cumplir al menos 1 condicion
    Operador NOT    -> Invierte el valor de True/False y viceversa
"""

usuario_autenticado = True
usuario_admin = False

if usuario_autenticado and usuario_admin:
    print('Acceso como Administrador')
elif usuario_autenticado:
    print('Acceso como Usuario')
else:
    print('Debes iniciar sesion')