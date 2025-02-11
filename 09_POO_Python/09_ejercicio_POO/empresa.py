from empleado import Empleado

class Empresa:

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
    
    # Método crear un empleado
    def contratar_empleado(self, nombre, departamento):
        # Creacion de un empleado
        empleado = Empleado(nombre, departamento)
        # Agregando al nuevo empleado al array
        self.empleados.append(empleado)

    # Método obtener empleados por departamento 
    def empleados_por_departamento(self, departamento):
        # Variable de instancia
        contador_empleados_por_departamento = 0
        # Iteracion de la lista empleados
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados_por_departamento += 1
        return contador_empleados_por_departamento

