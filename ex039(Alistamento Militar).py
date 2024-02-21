from datetime import date

sexo = str(input('Você é do Sexo masculino ou feminino, Digite (M) ou (F):')).upper()

if sexo == 'F':
    print('Seu alistamento não é obrigatório.')
    opcao = str(input('Mas se você quiser se alistar Digite (S), e se realmente NÃO quiser Digite (N):')).upper()

    if opcao == 'N':
        exit(print('Obrigado por ter vindo, quando estiver preparado e ainda estiver na idade pode voltar.'))

anoDigitado = int(input('Qual Ano do Seu nascimento: '))

anoAtual= date.today().year

verificaoAlistamento = anoAtual - anoDigitado

dataLimite = anoDigitado + 22

if verificaoAlistamento >= 18 and verificaoAlistamento < 23:#verifica se tem idade maior ou igual a 18 e menor 23.
    print(f'Você está com {verificaoAlistamento} anos de idade, e pode se Alistar.')

elif verificaoAlistamento > 22:#verifica se tem idade maior que 22
    print(f'Você tem {verificaoAlistamento} anos de idade e infelizmente não poderá se Alistar.\n'
          f'Você deveria ter se alistado há {anoAtual - dataLimite} anos atrás.\n'
          f'Sua data Limite de Alistamento foi no Ano de {anoAtual - (verificaoAlistamento-22)}')
    
else:#verifica se tem idade menor que 18.
    print(f'Você está com {verificaoAlistamento} anos de idade e ainda é muito novo para se Alistar.\n'
          f'Você terá que esperar mais {(anoDigitado + 18) - anoAtual} ano(s).\n'
          f'Você terá idade sulficiente no Ano de {anoDigitado + 18}')
