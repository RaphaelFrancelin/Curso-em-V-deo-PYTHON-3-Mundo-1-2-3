numero= 0
while True:
    numero = int(input('Qual número quer ver a Tabuada: '))
    if numero < 0:
        print('Fim do Programa')
        break
    for c in range(1,11):
        print(f'{numero} X {c} = {numero * c}')
