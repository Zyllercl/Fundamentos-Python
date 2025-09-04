"""
Uso de los Atributos de Clases
==============================
Este script muestra la diferencia entre un Atributo de Instancia (Objeto) y Atributo de Clase.
"""

class Persona:
    # --------------------------------
    # Creación de los Atributos de Clase
    # --------------------------------
    atributo_clase = 0
    
    # --------------------------------
    # Creación del Constructor
    # --------------------------------
    def __init__(self, atributo_instancia):
        # --------------------------------
        # Creación de los Atributos de Instancia
        # --------------------------------
        self.atributo_instancia = atributo_instancia
    

if __name__ == '__main__':
    print(f'[ATRIBUTOS DE CLASE]\n')

    print(f'[ORIGINAL] Atributo de la Clase: {Persona.atributo_clase}')

    # --------------------------------
    # Modificando el 'Atributo de Clase'
    # --------------------------------
    Persona.atributo_clase = 10 

    print(f'[MODIFICADO] Atributo de la Clase: {Persona.atributo_clase}\n')

    # --------------------------------
    # Creación del primer objeto
    # --------------------------------
    persona1 = Persona(20) # El valor 20 va al "atributo_instancia"
    
    print(f'Atributo de Clase desde "persona1" (objeto): {persona1.atributo_clase}') # NO RECOMENDADO

    print(f'Atributo de Instancia desde "persona1" (objeto): {persona1.atributo_instancia}\n')

    # --------------------------------
    # Creación del segundo objeto
    # --------------------------------
    persona2 = Persona(50) # Usa el constructor para inicializar atributos de instancia

    # persona2.atributo_clase = 30  -> Crea nuevo atributo de instancia (NO RECOMENDADO)
    
    print(f'Atributo de Clase desde "persona1" (objeto): {persona2.atributo_clase}') # NO RECOMENDADO

    print(f'Atributo de Instancia desde "persona1" (objeto): {persona2.atributo_instancia}')
