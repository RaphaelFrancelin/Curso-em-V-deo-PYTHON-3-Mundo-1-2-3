for c in range (1, 10):
    print(c)
print('Fim do for')

c=1
while c < 10:
    print(c)
    c+=1
print('Fim do while')

n=1
while n!=0:
    n = int(input('Digite um valor ou digite 0 para parar:'))
print('Fim do while')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim do while')


numero = 1
pares = 0
impares = 0
while numero != 0:
    numero = int(input('Digite um valor e vamos analisar quantos são pares e ímpares: (Digite 0 para parar)'))
    if numero != 0:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'Você digitou {pares} números pares e {impares} números ímpares.')
