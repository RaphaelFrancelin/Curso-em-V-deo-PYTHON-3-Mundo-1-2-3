numero = int(input('Digite o Número: '))

unidade = numero//1 % 10
print(f'Unidade = {unidade}')

dezena = numero//10 % 10
print(f'Dezena = {dezena}')

centena = numero//100 % 10
print(f'Centena = {centena}')

milhar = numero//1000 % 10
print(f'Milhar = {milhar}')
