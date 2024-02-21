from time import sleep

primeiroValor = int(input('Digite o Primeiro valor: '))
segundoValor = int(input('Digite o Segundo Valor: '))

opcao = 0

while opcao != 5:
    print('O que deseja Fazer?\n'
          '[1] para Somar\n'
          '[2] para Multiplicar\n'
          '[3] para Maior\n'
          '[4] para novos Números\n'
          '[5] para sair do Programa.')
    opcao = int(input('Qual sua Opção? '))
    if opcao == 1:
        print('_-_-' * 15)
        print(f'A soma de {primeiroValor} mais {segundoValor} é igual à {primeiroValor + segundoValor}.')
        print('_-_-'*15)
    elif opcao == 2:
        print('_-_-' * 15)
        print(f'A mutiplicação de {primeiroValor} vezes {segundoValor} é igual à {primeiroValor * segundoValor}.')
        print('_-_-' * 15)
    elif opcao == 3:
        if primeiroValor > segundoValor:
            print('_-_-' * 15)
            print(f'O número {primeiroValor} é maior que o número {segundoValor}.')
            print('_-_-' * 15)
        elif primeiroValor < segundoValor:
            print('_-_-' * 15)
            print(f'O número {segundoValor} é maior que o número {primeiroValor}.')
            print('_-_-' * 15)
        else:
            print('_-_-' * 15)
            print('Os números escolhidos são iguais')
            print('_-_-' * 15)
    elif opcao == 4:
        print('_-_-' * 15)
        print('Digite Novos Valores.')
        primeiroValor = int(input('Digite o Primeiro valor: '))
        segundoValor = int(input('Digite o Segundo Valor: '))
    elif opcao == 5:
        print('_-_-' * 15)
        print('Programa Encerrado.')
        print('_-_-' * 15)
        exit()
    else:
        print('_-_-' * 15)
        print('Opção inválida tente outra vez.')
        print('_-_-' * 15)
    sleep(2)
