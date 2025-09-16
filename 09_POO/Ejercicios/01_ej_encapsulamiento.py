"""
Ejemplo: Encapsulamiento Métodos GET y SET
==========================================
Este script muestra la forma en que se declara un Método GET y SET (sintaxis y recomendaciones)

Forma básica para crear una función GET y SET:

    [MÉTODO GET] Obtener el valor del Atributo

        def get_marca(self):
            return self._marca

        def get_modelo(self):
            return self._modelo

        def get_color(self):
            return self._color

    [MÉTODO SET] Cambiar el valor del Atributo

        def set_marca(self, marca):
            self._marca = marca
        
        def set_modelo(self, modelo):
            self._modelo = modelo
        
        def set_color(self, color):
            self._color = color
"""

# --------------------------------
# Declacación de la Clase
# --------------------------------
class Bicicleta:
    # --------------------------------
    # Creación del Constructor
    # --------------------------------
    def __init__(self, marca, modelo, color):
        # --------------------------------
        # Creación de Atributos de Instancia (Protegidos)
        # --------------------------------
        self._marca = marca         # Atributos Protegidos (NO MODIFICAR)
        self._modelo = modelo       # Atributos Protegidos (NO MODIFICAR)
        self._color = color         # Atributos Protegidos (NO MODIFICAR)


    # --------------------------------
    # Creación de Método de Instancia
    # --------------------------------

    # Método para Mostrar Info
    def informacion(self):
        print(f'[INFO] Marca: {self._marca} , Modelo: {self._modelo} , Color: {self._color}\n')

    # --------------------------------
    # Creación Método GET [RECOMENDADO]
    # --------------------------------
    @property # 
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo
    
    @property
    def color(self):
        return self._color

    # --------------------------------
    # Creación Método SET [RECOMENDADO]
    # --------------------------------
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    
    @color.setter
    def color(self, color):
        self._color = color


if __name__ == '__main__':
    print(f'[ENCAPSULAMIENTO - MÉTODOS GET Y SET]\n')
    # --------------------------------
    # Creación del Objeto
    # --------------------------------
    bicicleta = Bicicleta('Sparta', 'Rutera', 'Negro')

    # --------------------------------
    # Mostrando Info del Objeto
    # --------------------------------
    print(f'[~Información Original~]')
    bicicleta.informacion()

    # --------------------------------
    # Modificación con el Método SET
    # --------------------------------
    bicicleta.color = 'Plateado'        # [!] Se manda a llamar la funcion como atributo
    bicicleta.marca = 'Decathlon'
    bicicleta.modelo = 'Montaña'

    # --------------------------------
    # Agregando un Nuevo Atributo [NO DEFINIDO EN LA CLASE]
    # --------------------------------
    setattr(bicicleta, 'nuevo_atributo', 'valor nuevo atributo agregado')   # Forma 1
    print(f'[FORMA 1] Nuevo Atributo: {bicicleta.nuevo_atributo}\n')
    
    # --------------------------------
    # Agregando un Nuevo Atributo de manera Dinámica
    # --------------------------------
    bicicleta.nuevo_atributo2 = 'Este es otro atributo'                     # Forma 2
    print(f'[FORMA 2] Nuevo Atributo Dinámico: {bicicleta.nuevo_atributo2}\n')

    # --------------------------------
    # Mostrando Info Modificada
    # --------------------------------
    print(f'[~Información Modificada~]')
    bicicleta.informacion()

    # --------------------------------
    # Obtener los Atributos de un Objeto
    # --------------------------------
    print(f'[ATRIBUTOS] Obteniendo atributos de Bibicleta: {bicicleta.__dict__}\n')
    
    # --------------------------------  
    # Obtener un Atributo X desde la función con Decorador (Ej: Marcca)
    # --------------------------------
    print(f'[ATRIBUTOS] La "Marca" de la Bicicleta es: {bicicleta.marca}\n')

    # -------------------------------- 
    # Creación de otro Objeto
    # -------------------------------- 
    bibicleta_pistera = Bicicleta('Bianchi', 'Pistera', 'Morado')

    print(f'[ATRIBUTOS] Bicicleta Pistera: {bibicleta_pistera.__dict__}\n')
