cont = 1
while cont <= 10:
    print(cont, ' => ', end='')
    cont += 1
print('Acabou')

n = 0
s = 0
while True:
    n = int(input('Digite um Número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') # PYTHON 3.6+
print('O {} tem {} anos.'.format(nome,idade)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2