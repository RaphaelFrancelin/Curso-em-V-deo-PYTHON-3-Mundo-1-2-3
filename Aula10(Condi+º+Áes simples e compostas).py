tempo= int(input('Quantos anos tem seu carro: '))
if tempo <=3:
    print('Seu carro é novo')
else:
    print('Seu carro é vellho')
print('FIM')

print('Seu carro é novo' if tempo <= 3 else 'Seu carro é vellho')#Condição Simplificada
print('FIM')

nome= str(input('Qual seu Nome? '))
if nome == 'Raphael':
    print('Que nome lindo você tem! ')
else:
    print('Seu Nome é tão normal')
print(f'Bom dia, {nome}')


nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
media= (nota1+nota2)/2
print(f'Sua Média é {media}')
if media >= 6.0:
    print('Parabéns sua media foi boa')
else:
    print('Sua media foi ruim, estude mais')

print('Parabéns' if media >= 6.0 else 'Estude mais')#Condição simplificada