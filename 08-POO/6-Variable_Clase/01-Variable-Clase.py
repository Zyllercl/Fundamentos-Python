"""
    Metodos estaticos   -> Se asocian a una clase con si misma
                        -> No pueden acceder a variables de instancia (atributos), ya que se crean al momento de definir un objeto
                        -> Cuando se trabaja con la clase es de metodo estatico
                        -> No se puede acceder a self ya que esta realicionada con los objetos
                        
    Metodo Dinamico     -> Cuando se trabaja con objetos, una vez cargada la clase
    
    
    Al momento de que se cargue la clase en memoria, en el contexto dinamico un objeto SI puede acceder al contexto estatico (las clases), pero las clases (contexto estatico) NO pueden acceder al contexto dinamico
""" 

class MiClase:
    # Variables
    variable_clase = 'Valor variable clase'
    
    def __init__(self, variable_instancia):
        # Cada variable_instancia se asocia a cada objeto y cada objeto tiene su propio valor (no se comparte esta variable)
        self.variable_instancia = variable_instancia

    # Metodos estaticos
    @staticmethod
    def metodo_estatico():
        # Acceder a la variable de clase de manear indirecta
        print(MiClase.variable_clase)
    
    # Metodos de clase
    @classmethod
    def metodo_clase(cls):
        # Acceder a la variable_clase
        print(cls.variable_clase)
    
    # Metodo de instancia
    def metodo_instancia(self):
        # Un metodo de instancia puede acceder a un classmethod o staticmethod
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

# Uso de metodo estatico
print('Metodo Estatico'.center(50,'-'))
MiClase.metodo_estatico()

# Uso de metodo de clase
print('Metodo Clase'.center(50,'-'))
MiClase.metodo_clase()

# Creacion de un objeto
print('Creacion de un objeto'.center(50,'-'))
miObjeto = MiClase('Valor variable instancia')
miObjeto.metodo_clase()

miObjeto.metodo_instancia()

""" 
print(MiClase.variable_clase)

# Objeto 1
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

# Se puede definir una nueva variable dentro de una clase en cualquier momento
miClase.variable_clase2 = 'Valor variable clase 2'

# Objeto 2
miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

print(miClase.variable_clase2)
"""