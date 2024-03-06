
# Entrada de datos

"""
    Se utiliza la funcion 'input()' para detener la ejecución del programa hasta que el usuario agregue información por teclado.
    Las entradas de datos SIEMPRE vienen en String!!!
    \r\n -> Salto de linea
"""

# Variales
nombre = input('Cual es tu nombre: ')

print(f'Hola {nombre}')

# Leer datos que son numeros
edad = input('Cual es tu edad: ')
# Convertir edad (string) a int
edad = int(edad)

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

# Mezclando con operadores
numero = input('Agrega un numero y te dire si es par o impar: ')
numero = int(numero)

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')

# Reto # 
"""
    Realizar un examen con 3 preguntas, el usuario debera responder "Si" o "No" y al final otorgarle una calificacion (La calificacion se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1)
"""

print('[!] Examen Final')
print('Responder con "Si" o "No"')

# Variables
puntaje = 0
pregunta1 = input('Te gusta el helado: ')
pregunta2 = input('Te gusta la pizza: ')
pregunta3 = input('Te gusta la bebida: ')

if pregunta1 == "Si": 
    puntaje += 1
else:
    puntaje += 0

if pregunta2 == "Si":
    puntaje += 1
else:
    puntaje += 0

if pregunta3 == "Si":
    puntaje += 1
else:
    puntaje += 0

print(f'Tu puntaje es de {puntaje}')




