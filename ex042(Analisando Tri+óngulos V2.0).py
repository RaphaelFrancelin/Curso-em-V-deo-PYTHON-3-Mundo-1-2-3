reta1 = float(input('Digite o comprimento da primeira Reta: '))
reta2 = float(input('Digite o comprimento da Segunda Reta: '))
reta3 = float(input('Digite o comprimento da terceira Reta: '))

if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:

    if reta1 == reta2 == reta3:
        print('Formam um triângulo equilátero')

    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('Formam um triângulo Isósceles')

    else:#r1 != r2 != r3 != r1
        print('Formam um triângulo escaleno')
else:
    print('Não formam um triângulo')