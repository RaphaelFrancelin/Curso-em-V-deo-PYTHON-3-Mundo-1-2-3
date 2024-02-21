num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)#adicionou o 7 na ultima posição
print(num)
num.sort()#organiza a lista
print(num)
num.sort(reverse=True)#inverte a lista
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)#insere o elemento 0 na segunda posição
print(num)
num.pop()#remove na ultima posição
print(num)
num.remove(3)#vai percorrer a lista e remover o primeiro 3 que encontrar, porém se não tiver o numero escrito, retorna ERRO.
print(num)
if 8 in num:
    num.remove(8)# se precisar remover um número, e não tem como garantir que ele esteje na lista, essa melhor forma.
else:
    print('Não achei o número 8')
print(num)

print("-="*40)
print(f'{"Nova lista1":^30}')
print("-="*40)

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao Fim da lista')

print("-="*40)
print(f'{"Nova lista2":^30}')
print("-="*40)

valores1 = list()
for cont in range(0, 5):
    valores1.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores1):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao Fim da lista')

print("-="*40)
print(f'{"Nova lista3":^30}')
print("-="*40)

a  = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print("-="*40)

b[2] = 8# quando feito isso foi criado uma ligação entre A e B, por isso,
            # que uma espelha na outra, por isso não alterou a posição 2 somente do B

print(f'Lista A: {a}')
print(f'Lista B: {b}')
print("-="*40)

b = a[:] #para não terem ligação tem ser escrito assim, com fatiamento, aqui foi feito uma copia de A.
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print("-="*40)