import os

# Variables
CARPETA = 'contactos/' # Carpeta de contactos
EXTENSION = '.txt' # Extension del archivo

# Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # Revisa si la carpeta existe o no
    crear_directorio()
    # Muestra el menu de opciones
    mostrar_menu()
    # Preguntar al usuario la accion a realizar
    preguntar = True

    while preguntar:
        opcion = input('Seleccione una opcion: ')
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo!')


def agregar_contacto():
    print('Agrega un nuevo contacto')
    nombre_contacto = input('Ingrese nombre: ')

    # Validar si el archivo ya existe
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Campos de contacto
            telefono_contacto = input('Ingresa telefono: ')
            categoria_contacto = input('Ingresa categoria: ')
            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('Telefono: ' + contacto.telefono + '\n')
            archivo.write('Categoria: ' + contacto.categoria + '\n')
            # Mostrar mensaje de exito
            print('Contacto creado correctamente \n')
    else:
        print('[!] El contacto ya existe!!!')
    
    # Reiniciar la app
    app()

def editar_contacto():
    nombre_anterior = input('Escribe el nombre del contacto a editar: ')

    # Validar si el archivo ya existe
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            # Campos de contacto
            nombre_contacto = input('Agregar nuevo nombre: ')
            telefono_contacto = input('Agregar nuevo telefono: ')
            categoria_contacto = input('Agregar nueva categoria: ')

            # Instanciar 
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('Telefono: ' + contacto.telefono + '\n')
            archivo.write('Categoria: ' + contacto.categoria + '\n')

            # Cerrar archivo
            archivo.close()

            # Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # Mostrar mensaje de exito
            print('Contacto editado correctamente \n')
    else:
        print('[!] El contacto ingresado no existe')

    # Reiniciar la App
    app()

def mostrar_contactos():
    # Listar archivos de un directorio
    archivos = os.listdir(CARPETA)

    # Recorrer los archivos solo los que contengan .txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime el contenido del archivo
                print(linea.rstrip())
            print('\n')

def buscar_contacto():
    nombre = input('Ingrese el contacto que desea buscar: ')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\nInformacion del contacto:\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\n')
    except IOError:
        print('[!] El archivo no existe! \n')

    # Reiniciar app
    app()

def eliminar_contacto():
    nombre = input('Ingrese el contacto que desea eliminar: ')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado correctamente\n')
    except:
        print('[!] El contacto no existe! \n')

    # Reiniciar app
    app()
    
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto\n')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear carpeta
        os.makedirs(CARPETA)
    
app()