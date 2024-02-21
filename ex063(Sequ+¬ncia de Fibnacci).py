numero = int(input('Quantos números deseja ver a Sequência de Fibonacci: '))

n1 = 0
n2 = 1
print(f'{n1} => {n2} => ', end='')

contador = 3

while contador <= numero:
    n3 = n1 + n2
    print(f'{n3} => ', end='')
    n1 = n2
    n2 = n3
    contador += 1
print('Acabou')
