numero= int(input('Escolha um Número que te mostro se é impar ou par: '))

resto = numero % 2 # O resto de qualquer divisão por 2 é 0 se for par e 1 se for impar

if resto == 0:
    print(f'O Número {numero} é Par.')
else:
    print(f'O Número {numero} é Impar.')