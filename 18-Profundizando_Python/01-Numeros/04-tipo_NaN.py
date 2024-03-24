# Sistemas de Numeracion 'Not a Number' con Python Avanzado

import math
from decimal import Decimal

# Definicion de un tipo Not a Number (NaN)
a = float('NaN')
print(f'a: {a}')
print(f'Es NaN (Not a Number)?: {math.isnan(a)}')

b = Decimal('NaN')
print(f'a: {b}')
print(f'Es NaN (Not a Number)?: {math.isnan(b)}')
