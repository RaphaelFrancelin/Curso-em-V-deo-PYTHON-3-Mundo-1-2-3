from random import randint

print('Sou seu computador...')
print('Acabei de escolher um numero entre 0 e 10.')
print('Será que vc consegue adivinhar?')
escolha = (int(input('Qual seu chute? ')))
computador = randint(0,10)
contador = 0

while escolha != computador:
    if escolha > computador:
        escolha = (int(input('Errouuu, tente um numero menor: ')))
        contador += 1
    if escolha < computador:
        escolha = (int(input('Errouuu, tente um numero maior: ')))
        contador += 1
if contador == 0:
    print('Caraca vc acertou de Primeira!!!')
else:
    print(f'Parabéns vc acertou com {contador} chute(s)')