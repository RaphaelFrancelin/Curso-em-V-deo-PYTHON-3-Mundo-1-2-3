reta1 = float (input('Digite a primeira reta: '))
reta2 = float (input('Digite a segunda reta: '))
reta3 = float (input('Digite a terceira reta: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('Essa condição formam um triângulo')
else:
    print('Essa condição não formam um triângulo')