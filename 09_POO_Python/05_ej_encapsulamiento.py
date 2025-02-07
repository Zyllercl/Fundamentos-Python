'''
    ENCAPSULAMIENTO: METODOS GET Y SET

        # Método GET (sirve para obtener el valor del atributo)

            * Forma básica de crear una funcion GET
                
                def get_marca(self):
                    return self._marca
            
            * Forma recomendada para crear una funcion GET

                @property
                def marca(self):
                    return self._marca
            
            * Forma básica de crear una funcion SET

                def set_marca(self, marca):
                    self._marca = marca
            
            * Forma recomendada para crear una funcion SET

                @marca.setter
                def marca(self):
                    self._marca = marca

                Donde:
                    @{atributo}.setter  -> Consiste en cambiar un atributo dentro de una clase
'''

# Declaración de la clase
class Bicicleta:

    # Constructor
    def __init__(self, marca, modelo, color):
        # Atributos protegidos (NO SE DEBEN MODIFICAR)
        self._marca = marca
        self._modelo = modelo
        self._color = color

    # Mostrar info de la bicicleta
    def informacion(self):
        print(f'''Información Bicicleta
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}
        ''')

    # Método GET (sirve para obtener el valor del atributo)
    '''
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_color(self):
        return self._color
    '''

    # Decorador Property: es una propiedad de la clase
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo
    
    @property
    def color(self):
        return self._color

    # Método SET (sirve para cambiar el valor del atributo)
    '''
    def set_marca(self, marca):
        self._marca = marca
    
    def set_modelo(self, modelo):
        self._modelo = modelo
    
    def set_color(self, color):
        self._color = color
    '''
    
    # Decorador setter: es una propiedad de la clase
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
    # Creacion del objeto bicicleta rutera
    bicicleta_rutera = Bicicleta('Sparta', 'Rutera', 'Negro')
    # Informacion Base
    print('[!] Info Original')
    bicicleta_rutera.informacion()

    # Modificar un parametro con el método SET creado
    bicicleta_rutera.color = 'Plateado' # [!] Se manda a llamar la funcion como atributo
    bicicleta_rutera.marca = 'Decathlon'
    bicicleta_rutera.modelo = 'Montaña'

    # Agregar un nuevo atributo (NO definido en la clase)
    setattr(bicicleta_rutera, 'nuevo_atributo', 'valor nuevo atributo agregado') # Forma 1
    # Agregar un nuevo atributo de forma dinámica
    bicicleta_rutera.nuevo_atributo2 = 'Este es otro atributo' # Forma 2

    # Información Modificada
    print('[!] Info Modificada')
    bicicleta_rutera.informacion()

    # Mostrar nuevos atribuutos agregados dinamicamente
    print(f'{bicicleta_rutera.nuevo_atributo}\n')
    print(f'{bicicleta_rutera.nuevo_atributo2}\n')

    # Obtener los atributos de un objeto
    print(f'[ATRIBUTOS] Bicicleta Rutera: {bicicleta_rutera.__dict__}')
    # Obtener el atributo 'marca' desde la funcion con decorador
    print(f'\nLa marca de la Bicicleta es: {bicicleta_rutera.marca}')


    # Creacion del objeto bibicleta pistera
    bibicleta_pistera = Bicicleta('Bianchi', 'Pistera', 'Morado')
    print(f'\n[ATRIBUTOS] Bicicleta Pistera: {bibicleta_pistera.__dict__}')
