velocidade= int(input('Qual velocidade do seu carro está? '))

if velocidade > 80:
    valorMulta= (velocidade - 80) * 7
    print(f'Multado! Você excedeu o limete permitido de 80km/h '
          f'Você deve pagar uma multa R${valorMulta:.2f}!')

print('Tenha um Bom dia! Dirija com segurança!')
