
maiorPeso = 0
menor = 0

for repeticao5x in range(1,6):
    peso = float(input(f'Qual peso da {repeticao5x}ª pessoa: '))
    if repeticao5x == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
        print(f'maior Peso {maiorPeso} e menor Peso {menorPeso}.')






