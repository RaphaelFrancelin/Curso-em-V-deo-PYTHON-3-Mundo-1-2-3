nome = str(input('Qual seu Nome?'))

if nome == 'Raphael':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cládia Jéssica Juliana':
    print('Belo nome feminino!!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um ótimo dia {nome}...')