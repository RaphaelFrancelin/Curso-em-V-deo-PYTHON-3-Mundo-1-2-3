#Tuplas = ()
#Listas = []
#Dicionários = {}

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items(): # k = keys e v = values
    print(f'{k} = {v}')

print(f'{"-"*8} adicionando um item no dicionário {"-"*8}')
pessoas['peso'] = 98.5 #adicionando um item no dicionário
for k, v in pessoas.items(): # k = keys e v = values
    print(f'{k} = {v}')

print(f'{"-"*8} trocando o nome Gustavo para Leandro {"-"*8}')
pessoas['nome'] = 'Leandro' #trocando o nome Gustavo para Leandro
for k, v in pessoas.items(): # k = keys e v = values
    print(f'{k} = {v}')

print(f'{"-"*8} apagando um item do dicionário {"-"*8}')
del pessoas['sexo'] #apagando um item do dicionário
for k, v in pessoas.items(): # k = keys e v = values
    print(f'{k} = {v}')

print('_'*30)
estado = dict()
brasil = list()

for c in range (0, 3):
    estado['uf'] = str (input('Unidade Federativa: '))
    estado['sigla'] = str (input('Sigla do Estado: '))
    brasil.append(estado.copy())# esse .copy equivale ao [:], isso faz com que não crie vinculo com a lista principal.
for e in brasil:
    print(e)
print('_'*30)
for e in brasil: #esse for é da lista
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')
print('_'*30)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
