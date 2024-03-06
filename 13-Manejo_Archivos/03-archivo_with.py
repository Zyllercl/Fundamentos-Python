
# Sintaxis: Context Manager (Administrador de Recursos)
""" 
    El metodo WITH llama a dos metodo:
        - __enter__ : Metodo que abre el recurso (archivo)
        - __exit__  : Metodo que cierra automaticamente el recurso (archivo)
    
    Definiciones:
        - with -> Se manda a llamar el metodo __enter__ de la clase ManejoArchivos
        - Al terminar el bloque de codigo del 'with', se manda a llamar automaticamente el metodo __exit__ de la clase ManejoArchivos
"""
""" 
    # Ejemplo de metodo With
    
    with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read()) 
"""

from ejemplo_ManejoArchivos import ManejoArchivos

# Utilizacion de la clase ManejoArchivos
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())