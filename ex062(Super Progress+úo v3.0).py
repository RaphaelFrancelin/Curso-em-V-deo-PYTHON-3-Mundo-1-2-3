primeiroTermo = int(input('Qual o primeiro Termo: '))
razao = int(input('Qual a Razão: '))
contador = 1
progressao = 10
valorAcrescentado = 0

while progressao != 0:
    valorAcrescentado = valorAcrescentado + progressao
    while contador <= valorAcrescentado:
        print(f'{primeiroTermo} => ', end='')
        primeiroTermo += razao
        contador += 1
    print('Acabou? ')
    progressao = int(input('Quantos termos vc deseja Adicionar? '))
print('Fim do Programa....')
print(f'Esse Programa te mostrou {valorAcrescentado} Termos.')
