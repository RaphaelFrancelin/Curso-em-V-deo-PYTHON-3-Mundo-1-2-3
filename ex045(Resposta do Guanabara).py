from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Sua Opções:\n'
'[0] PEDRA\n'
'[1] PAPEL\n'
'[2] TESOURA')
jogador = int(input('Qual sua Opção? '))
print('-='*11)
print(f'Jogador jogou {itens[jogador]}')
print(f'Computador jogou {itens[computador]}')
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')
