numero = int(input('Digite um número e se quiser parar Digite 999: '))

n1 = 0
soma = 0
contador = 0
while numero != 999:
    n1 = numero
    soma = soma + n1
    contador += 1
    numero = int(input('Digite um número e se quiser parar Digite 999: '))

print(f'Você Digitou {contador} números e a soma deles é de {soma}.\n'
      f'Fim do Programa....')
