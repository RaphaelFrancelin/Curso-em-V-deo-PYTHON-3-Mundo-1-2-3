
somaDaMediaDeIdade = 0
mediaDeIdade = 0

maiorIdadeHomem = 0
nomeDoMaisVelho = ''

contadorSexoFeminino = 0

for pessoas in range (1,5):
    print(f'----- {pessoas}ª PESSOA -----')
    nome = str(input('Nome: ')).rstrip().lstrip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    somaDaMediaDeIdade += idade

    if sexo == 'F' and idade < 20:
        contadorSexoFeminino += 1

    if pessoas == 1 and sexo in 'M':
        maiorIdadeHomem = idade
        nomeDoMaisVelho = nome
    if idade > maiorIdadeHomem and sexo in 'M':
            maiorIdadeHomem = idade
            nomeDoMaisVelho = nome

mediaDeIdade = somaDaMediaDeIdade / 4

print(f'A idade Média do grupo é de {mediaDeIdade}.')
print(f'A pessoa do Sexo Masculino mais velha tem {maiorIdadeHomem} anos de idade e seu Nome é {nomeDoMaisVelho}.')
print(f'E {contadorSexoFeminino} pessoas de Sexo Feminino do Grupo tem menos de 20 anos.')
