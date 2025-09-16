"""
Clase Object en Python
======================
Este script muestra un ejemplo de la estructura y como funciona la Clase Object en Python.

Descripción del método Super():
    -  El método super() permite acceder a los métodos de la clase padre (heredada desde object) desde la clase hija.
    - En este ejemplo, se usa super().__str__() para llamar al método __str__ de object, que por defecto devuelve la dirección de memoria del objeto.
"""

# ----------------------
# Creación de Clase
# ----------------------
class Persona:
    # ----------------------
    # Sobreescritura del Método init (Heredandolo de la Clase Object)
    # ----------------------
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # ----------------------
    # Sobreescritura del Método str
    # ----------------------
    def __str__(self):
        mensaje = (f'[PERSONA] Nombre: {self.nombre} - Apellido: {self.apellido} - Dir. Memoria: {super.__str__(self)}')
        return mensaje

# ----------------------
# Testing Clase Object
# ----------------------

# Creación del Objeto Persona
persona = Persona('Tash', 'Sultana')
print(persona)      # Se llama automaticamente el método __str__ desde print()