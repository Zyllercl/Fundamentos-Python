
# Creación de una clase para manejar archivos
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __enter__(self):
        print(f'[INFO] Obteniendo recurso desde ManejoArchivos'.center(50, '-'))

        # Abrir el archivo en modo lectura
        self.nombre = open(self.nombre, 'r', encoding='utf-8')

        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        print(f'[INFO] Liberando recurso desde ManejoArchivos'.center(50, '-'))

        if self.nombre:
            # Cerrar el archivo
            self.nombre.close()