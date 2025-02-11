
class Empleado:

    # Atributo de Clase
    contador_empleados = 0

    def __init__(self, nombre, departamento):
        # Atributos de Instancia
        self.nombre = nombre
        self.departamento = departamento

        # Aumentando el contador en 1
        Empleado.contador_empleados += 1
    
    # Método de Clase
    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados