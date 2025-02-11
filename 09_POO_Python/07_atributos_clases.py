'''
    ATRIBUTOS DE CLASES

    Definicion de clase persona:

        ----------------------
                PERSONA
        ----------------------
           atributo_clase = 0
           atributo_instancia = 0    
    
    Donde:
        [!] La diferencia entre un atributo de clase e instancia se encuentra en la forma de acceder a ellos, es decir:

        - Atributo de clase     -> Los atributos de clase se accede directamente desde la clase (se encuentran fuera de los métodos). Además, se comparte la variable de atributo de clase para los distintos objetos que se vayan creando.
        - Atributo de instancia -> Los atributos de instancia se accede a través de un objeto (se definen los métodos)

        [*] Un 'objeto' puede acceder a los atributos de clase [*]
'''

class Persona:
    # Variables de Clase
    atributo_clase = 0

    def __init__(self, atributo_instancia):
        # Variables de Instancia
        self.atributo_instancia = atributo_instancia
    

if __name__ == '__main__':
    print(f'[~] Atributo de Clase\n')

    print(f'[ORIGINAL] Atributo de la Clase: {Persona.atributo_clase}')
    # Modificando el 'Atributo de Clase'
    Persona.atributo_clase = 10
    print(f'[MODIFICADO] Atributo de la Clase: {Persona.atributo_clase}\n')

    # Creacion de un Objeto
    persona1 = Persona(20)
    print(f'Atributo de Clase desde "persona1" (objeto): {persona1.atributo_clase}') # NO RECOMENDADO
    print(f'Atributo de Instancia desde "persona1" (objeto): {persona1.atributo_instancia}\n')

    persona2 = Persona(50)
    print(f'Atributo de Clase desde "persona1" (objeto): {persona2.atributo_clase}') # NO RECOMENDADO
    print(f'Atributo de Instancia desde "persona1" (objeto): {persona2.atributo_instancia}')
