numero = int(input('Digite um Número: '))

contador = 0

for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[33m',end='')
        contador += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO Número {c} foi dividido {contador} vezes, por isso ele ', end='')

if contador == 2:
    print('é primo', end='')
else:
    print('não é primo', end='')



