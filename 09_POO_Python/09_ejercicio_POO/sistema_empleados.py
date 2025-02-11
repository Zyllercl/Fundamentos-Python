from empresa import Empresa
from empleado import Empleado

print(f'[~~~~~ Sistema de Empleados ~~~~~]')

# Creacion instancia de una empresa
empresa_kmv = Empresa('KMV')

# Agregando nuevos empleados a la empresa KMV
empresa_kmv.contratar_empleado('Pepe', 'Bordador')
empresa_kmv.contratar_empleado('Vladimir', 'Reponedor')
empresa_kmv.contratar_empleado('Albert', 'Bordador')
empresa_kmv.contratar_empleado('Fran', 'Tecnico')

# Mostrar el total de objetos (tipo empleado
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

departamento_especifico = "Bordador" # Cambiar departamento

# Mostrar el total de empleados (Departamento en especifico)
print(f'[*] Empleados en el departamento de {departamento_especifico}: '
      f'{empresa_kmv.empleados_por_departamento(departamento_especifico)}')
