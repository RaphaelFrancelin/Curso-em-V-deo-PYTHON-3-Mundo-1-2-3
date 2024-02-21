nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua Media é {media:.1f} e você está Reprovado')

elif media >= 5.0 and media < 7:
    print(f'Sua Media é {media:.1f} e você está de Recuperação')

else:
    print(f'Sua Media é {media:.1f} e você está Aprovado')