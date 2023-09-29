#RAIZ QUADRADA
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.floor(raiz)}')

#POTENCIAÇÃO
from math import pow,floor
n1 = float(input('Digite um número para ser exponenciado:'))
n2 = float(input('Digite um número para ser exponencial:'))

print(f'O número ficará {n1.__pow__(n2)}')