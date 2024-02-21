for c in range(0, 6):
    print(c)
print('Fim')
print('-='*15)

for c in range(0, 6 +1):
    print(c)
print('Fim')
print('-='*15)

for c in range(6, 0, -1):
    print(c)
print('Fim')
print('-='*15)


for c in range(0, 6, 2):
    print(c)
print('Fim')
print('-='*15)


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):#O início é o número que deseja iniciar a contagem o fim é o final da contagem e o passo e número de casa que vai pular.
    print(c)
print('Fim')
print('-='*15)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
print('-='*15)

