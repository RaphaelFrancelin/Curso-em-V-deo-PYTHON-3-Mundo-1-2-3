from random import randint
numero = 0
jogador = 0
computador = 0
soma = 0
contador_de_vitorias = 0
condicaoPar = 0

fecharCores ='\033[m'
azul = '\033[34m'
vermelho = '\033[31m'

while True:
    jogador = str(input('Qual você escolhe Par[P] ou Ímpar[I]? ')).upper().strip()
    numero = int(input('Digite um Número: '))
    computador = randint(1,10)
    soma = numero + computador
    condicaoPar = soma % 2

    if condicaoPar == 0:
        condicaoPar = True
    else:
        condicaoPar = False

    if jogador == 'P' and condicaoPar == True:
        print(f'Você Jogou {numero} e o computador {computador} e a soma é de {soma}. Resultado é PAR')
        print(f'{azul}Você Ganhou{fecharCores}')
        print('Vamos Jogar novamente..')
        print(20*'#')
        contador_de_vitorias += 1
    else:
        print(f'Você Jogou {numero} e o computador {computador} e a soma é de {soma}. Resultado é ÍMPAR')
        print(f'{vermelho}Você Perdeu{fecharCores}')
        print(20*'#')
        print(f'Seu números de vitórias consecutivas foram de {contador_de_vitorias}.')
        print(20 * '#')
        print('Fim do Programa..')
        break
