import math

catetoOposto= float(input('Digite o comprimento do Cateto Oposto: '))
catetoAdjacente= float(input('Digite o comprimento do  Cateto Adjacente: '))

hipotenusa= math.hypot(catetoOposto, catetoAdjacente)

print(f'A Hipotenusa vai medir {hipotenusa:.2f}.')

