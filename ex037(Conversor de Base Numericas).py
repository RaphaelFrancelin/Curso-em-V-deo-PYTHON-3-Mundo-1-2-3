
valor = int(input('Digite o número inteiro a ser transformado: '))
print('''Escolha uma Base de Conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Qual sua opção: '))

if opcao == 1:
    print(f'{valor} convertido para BINÁRIO é igual a {bin(valor)[2:]}.')
elif opcao == 2:
    print(f'{valor} convertido para OCTAL é igual a {oct(valor)[2:]}.')
elif opcao == 3:
    print(f'{valor} convertido para HEXADECIMAL é igual a {hex(valor)[2:]}.')
else:
    print('Valor escolhido inválido, Tente com os valores citados.')


