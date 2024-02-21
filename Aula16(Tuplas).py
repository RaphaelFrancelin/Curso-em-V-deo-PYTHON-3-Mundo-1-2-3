# lanche = ()tupla  []lista  {}dicionário

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[0])
print(lanche[3])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-4])
print(lanche[-3:])
print(lanche[:-3])
print(lanche[::-1])
print(30*"=")

#lanche[1] = 'Refrigerante' não pode fazer esse comando por que as Tuplas são imutaveis

print(len(lanche))
print(30*"=")

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(30*"=")

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print(30*"=")

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')
print(30*"=")

print(sorted(lanche))#organiza em ordem alfabetica
print(30*"=")

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b
print(c)
c = b+a
print(c)

print(c.count(5)) #conta quantos 5 tem na tupla
print(c.index(8)) #mostra em qual posição o 8 se encontra, pega primeira ocorrência
print(c.index(5, 1)) #mostra em qualposição se encontra o 5 apartir do elemento 1


