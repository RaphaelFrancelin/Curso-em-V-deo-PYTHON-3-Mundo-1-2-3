from random import randint

opcao = int(input('[0] PEDRA\n'
                  '[1] PAPEL\n'
                  '[2] TESOURA\n'
                  'QUAL SUA OPÇÃO? '))

if opcao == 0:
    print('A sua opção é PEDRA')
elif opcao == 1:
    print('A sua opção é PAPEL')
elif opcao == 2:
    print('A sua opção é Tesoura')
else:
    print('Jogada invalida, jogue novamente.')
    exit()

computador = randint(0, 2)

if computador == 0:
    print('A opção do computador é PEDRA')
elif computador == 1:
    print('A opção do computador é PAPEL')
else:
    print('A opção do computador é Tesoura')

if opcao == computador:
    print('EMPATE')
elif opcao == 0 and computador == 1:
    print('O computador venceu')
elif opcao == 1 and computador == 2:
    print('O computador venceu')
elif opcao == 2 and computador == 0:
    print('O computador venceu')
else:
    print('Parabêns Você VENCEU!!')


