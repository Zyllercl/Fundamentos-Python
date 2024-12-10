'''
    ENTRADA DE DATOS POR CONSOLA

    Def:
        - La entrada de datos se realiza utilizando la función input(). Esta función pausa el programa y espera a que el usuario introduzca algún texto desde el teclado.
        - Los datos ingresados por consola son tratados como Strings (str)

    Características:
        - Interactividad:   Permite a los usuarios proporcionar valores dinámicos.
        - Sencillez:        Se necesita especificar en un mensaje que es lo que se esta solicitando al usuario.
        - Tipo de dato:     Todo dato ingresado por consola lo manejará en formato cadena (string). 
'''

'''     USO DE ENTRADA DE DATOS    '''
# Entrada de dato String
nombre_usuario = input('Ingresa nombre de usuario: ')
# Entrada de dato Númerico
edad_usuario = int(input('Ingresa tu edad: '))
# Entrada de dato Booleano
es_trabajador = input('¿Cargo de Jefe (Si/No)?: ')
# Entrada de dato Flotante
sueldo_usuario = float(input('Ingresa tu sueldo: '))
# Conversión de String a Booleano
es_trabajador = es_trabajador.lower() == 'si'

print('\n\t---DATOS INGRESADOS POR CONSOLA---\t\n')
print(f'Nombre Usuario: {nombre_usuario}')
print(f'Edad Usuario: {edad_usuario}')
print(f'Tiene Trabajo?: {es_trabajador}')
print(f'Sueldo Usuario: {sueldo_usuario:.2f}')



