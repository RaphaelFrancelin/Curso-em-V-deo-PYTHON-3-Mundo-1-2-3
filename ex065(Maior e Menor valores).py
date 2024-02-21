escolha = 's'
numeroMaior = 0
numeroMenor = 0
contador = 0
soma = 0
media = 0
while escolha == 's':
    numero = int(input('Digite um Número: '))
    escolha = str(input('Quer continuar com Programa [s/n]: ')).lower().strip()
    soma += numero
    contador += 1
    media = soma / contador
    if contador == 1:
        numeroMenor =numeroMaior = numero
    else:
        if numero > numeroMaior:
            numeroMaior = numero
        if numero < numeroMenor:
            numeroMenor = numero
print(f'Vc Digitou {contador} números e a Média é {media} e a soma {soma}.\n'
      f'O Número Maior digitado foi {numeroMaior} e o Número Menor foi {numeroMenor}.')
