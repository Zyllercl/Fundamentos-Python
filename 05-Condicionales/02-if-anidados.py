
# If Anidados

usuario_autenticado = False
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('Acceso como Administrador')
    else:
        print('Acceso denegado!')
else:
    print('Debes iniciar sesion')