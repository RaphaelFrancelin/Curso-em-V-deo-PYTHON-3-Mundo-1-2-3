nome = str(input('Qual seu Nome? '))

if nome == 'Raphael':
    print('Que nome Bonito você tem.')

elif nome == 'Pedro' or nome == 'João' or nome == 'Maria':
    print('Seu Nome é bem popular no Brasil.')

elif nome in 'Nayara Isadora Lorenzo':
    print('Pelo Nome você deve ser uma pessoa Muito Bonita.')

print(f'Tenha um Bom Dia {nome}!!!')