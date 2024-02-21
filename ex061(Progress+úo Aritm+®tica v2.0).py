print('='*20)
print('10 TERMOS DE UMA P.A.')
print('='*20)

primeiroTermo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))

contador = 1

while contador <= 10:
    print(f'{primeiroTermo} -> ', end='')
    primeiroTermo += razao
    contador += 1

print(f'Acabou...', end='')
