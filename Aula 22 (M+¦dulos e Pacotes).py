#
#
# FOI CRIADO PACOTES (em outras linguagens pacotes são chamdos de biblioteca)
# PACOTE CRIADO CHAMA UTEIS
#

from uteis import numeros
import math
num =int(input(('Digite um valor: ')))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
print(f'A raiz quadrada de {num} é {math.sqrt(num)}')
