from Empleado import Empleado
from Gerente import Gerente

# Metodo imprimir detalle
def imprimir_detalle(objeto):
    # print(objeto) # Llamada al objeto _str_
    print(type(objeto)) # Tipo de objeto
    print(objeto.mostrar_detalles())

# Creacion de empleado
empleado = Empleado('Raven', 5000)
imprimir_detalle(empleado)

# Creacion de una variable hacia la clase Hija
gerente = Gerente('Clarke', 7000, 'Sistemas')
imprimir_detalle(gerente)