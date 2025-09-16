
# -----------------------
# Definición de la Clase
# -----------------------
class Persona:
    # -----------------------
    # Constructor
    # -----------------------
    def __init__(self, nombre, edad):
        # -----------------------
        # Atributos de Instnacia
        # -----------------------
        self.nombre = nombre
        self.edad = edad
    
    # -----------------------
    # Sobrecarga del Operador Suma
    # -----------------------
    def __add__(self, other):
        # Se cambia la funcionalidad del método suma a "Sumar dos Personas (strings)"
        return f'{self.nombre} {other.nombre}'

    # -----------------------
    # Sobrecarga del Operador Resta
    # -----------------------
    def __sub__(self, otro):
        return self.edad - otro.edad

# -----------------------
# Ejemplo Sobrecarga Operador Suma
# -----------------------
# Objeto 1
persona_1 = Persona('Pepe', 30)
# Objeto 2
perosna_2 = Persona('Pepito', 18)
# Suma de los nombres con el operador + (Sobrecarga del Operador)
print(f'[SOBRECARGA] Suma: {persona_1 + perosna_2}')

# -----------------------
# Ejemplo Sobrecarga Operador Resta
# -----------------------
# Realiza la resta de la edad del objeto_1 y el objeto_2 teniendo en cuenta que se cambio la funcionalidad del Operador - (Sobrecarga del Operador)
print(f'[SOBRECARGA] Resta: {persona_1 - perosna_2}')
