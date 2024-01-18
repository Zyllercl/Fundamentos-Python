
# Ejercicio 

"""
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto y Bicicleta, estas deben heredar de la clase Padre vehiculo.
"""

class Vehiculo:
    def __init__(self, color, ruedas) -> None:
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self) -> str:
        return f'[Color: {self.color}, Ruedas: {self.ruedas}]'

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self) -> str:
        return f'Auto [Velocidad: {self.velocidad} (Km/h)] {super().__str__()}'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self) -> str:
        return f'Bicicleta [Tipo: {self.tipo}] {super().__str__()}'

# Creacion objeto tipo Vehiculo
vehiculo = Vehiculo('Verde', 4)
print(vehiculo)

# Creacion objeto tipo Auto
auto = Auto('Morado', 4, 300)
print(auto)

# Creacion objeto tipo Bicicleta
bicicleta = Bicicleta('Negro', 2, 'Biker')
print(bicicleta)