from math import factorial
numero = int(input('Qual número deseja ver o fatorial: '))
fatorial1 = factorial(numero)
print(f'O fatorial de {numero}! é {fatorial1}.')
print(f'Como é feito Fatorial de {numero}!.')

#Duas Maneiras de resolver o Fatorial

contador = numero
fatorial2 = 1 # Sempre que for trabalhar com mutiplicação a variavel não pode receber 0.

if contador == 0:
    print(f'O fatorial de {contador}! é {1}.')

while contador > 0:
    if contador > 1:
        print(f'{contador} X ', end='')
    elif contador == 1:
        print(f'{contador} = {fatorial2}', end='')
    fatorial2 *= contador
    contador -= 1


