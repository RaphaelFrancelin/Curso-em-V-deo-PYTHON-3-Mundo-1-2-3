peso = float(input('Qual seu Peso em Kilos: '))
altura = float(input('Qual sua altura em metros: '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu IMC é de {imc:.1f} e vc está Abaixo do Peso')

elif imc <= 25:
    print(f'Seu IMC é de {imc:.1f} e vc está no Peso Ideal')

elif imc <= 30:
    print(f'Seu IMC é de {imc:.1f} e vc está com Sobrepeso')

elif imc <= 40:
    print(f'Seu IMC é de {imc:.1f} e vc está com Obessidade')

else:
    print(f'Seu IMC é de {imc:.1f} e vc está com Obessidade Mórbida')