print('='*20)
print('10 TERMOS DE UMA P.A.')
print('='*20)

primeiroTermo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))

decimoTermo = primeiroTermo + (10-1) * razao

for c in range(primeiroTermo, decimoTermo+razao, razao):
    print(c, end= ' -> ')
print('ACABOU')




