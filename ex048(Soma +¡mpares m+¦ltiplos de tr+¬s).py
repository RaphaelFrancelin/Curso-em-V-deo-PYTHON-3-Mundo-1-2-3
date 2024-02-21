soma = 0
contador = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        soma = soma + c
        print(f'A soma de todos os numeros é {soma}')
        contador = contador + 1
        print(f'A contagem dos Numeros agora está {contador}')

print('-='*25)
print('SOLUÇÃO QUE O EXERCIO PEDE ESTÁ ABAIXO')
print('-='*25)

# Resolução que o exercicio pede

soma = 0
contador = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        contador = contador + 1
print(f'A soma de todos os {contador} números solicitados é {soma}.')
