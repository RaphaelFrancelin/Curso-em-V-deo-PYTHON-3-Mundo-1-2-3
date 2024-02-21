primeiroNumero = int(input('Digite o Primeiro Número: '))
segundoNumero = int(input('Digite o Segundo Número: '))

if primeiroNumero > segundoNumero:
    print(f'O Número {primeiroNumero} é maior que o Número {segundoNumero}.')

elif segundoNumero > primeiroNumero:
    print(f'O Número {segundoNumero} é maior que o Número {primeiroNumero}.')
    
else:
    print('Os Dois Números são Iguais')