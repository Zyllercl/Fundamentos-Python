# Sistemas de Numeracion con Python Avanzado

""" 
    SISTEMA     | BASE |    DIGITOS
    Binario     |  2   |      0,1         
    Octal       |  8   |   0,1,2,3,4,5,6,7
    Decimal     |  10  |  0,1,2,3,4,5,6,7,8,9
    Hexadecimal |  16  | 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
"""

# Decimal:
a = 10
# Binario:
a = 0b1010  # Numero binario equivalente a 10
# Octal:
a = 0o12    # Numero octal equivalente a 10
# Hexadecimal:
a = 0xA     # Numero hexadecimal equivalente a 10

        #   Conversion Base Numerica    #

# Convercion un tipo entero, incluyendo su base

# Base Decimal
a = int('23', 10)
# Base Binario
a = int('10111', 2)
# Base Octal
a = int('27', 8)
# Base Hexadecimal
a = int('17', 16)

# Base 5 (Valor 19 en decimal)
a = int('34', 5)

print(f'a: {a}')