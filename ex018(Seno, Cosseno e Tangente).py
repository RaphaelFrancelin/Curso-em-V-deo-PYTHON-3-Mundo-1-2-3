import math

angulo= float(input('Digite o ângulo: '))

seno= math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tangente= math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem o Seno de {seno:.2f}. \n'
      f'O ângulo de {angulo} tem o Cosseno de {cosseno:.2f}. \n'
      f'O ângulo de {angulo} tem o Tangente de {tangente:.2f}. ')