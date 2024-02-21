import random
import time

print('-=-'*20)
print('Vou pensar em um Numero de 0 à 5 tente adivinhar.... ')
print('-=-'*20)
numero = int(input('Escolha um Numero de 0 à 5: '))

numPc = random.randint(0, 5)

print('Processando...')
time.sleep(2)#tempo de espera antes de rodar o proximo codigo

if numero == numPc:
    print(f'Parabéns Você Ganhou, o seu numero escolhido {numero} e o que eu pensei é {numPc}!!!')
else:
    print(f'Eu GANHEI, você escolheu {numero} e eu pensei {numPc}, mais sorte da Próxima vez!!!')
