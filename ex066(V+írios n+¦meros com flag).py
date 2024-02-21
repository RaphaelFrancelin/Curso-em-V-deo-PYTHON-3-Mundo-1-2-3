numero = 0
contador = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número e quando quiser parar o Programa digite 999: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Vc Digitou {contador} números e somas entre eles é de {soma}.\n'
      f'Fim do programa.')
