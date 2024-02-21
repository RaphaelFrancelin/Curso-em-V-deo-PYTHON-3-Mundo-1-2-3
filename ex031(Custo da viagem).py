distancia = float(input('Qual a Distância da Viagem? '))

valorKm= 0.50

if distancia > 200:
    valorKm = 0.45

totalViagem = distancia * valorKm

print(f'Você iniciará uma viagem de {distancia}Km.'
      f'E o valor a ser pago é de R${totalViagem} ')