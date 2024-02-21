idade = 0
sexo = ""
continuar = str(input('Quer Iniciar o Cadastro? [S/N] ')).upper().strip()[0]
pessoas_de_maior = 0
homens = 0
mulheres = 0

while True:
    if continuar == 'S':
        print(f'{10*"-"}Cadastre uma pesoa{10*"-"}')
        idade = int(input("IDADE: "))

        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

        print(30*"-")
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]

        if idade >= 18:
            pessoas_de_maior += 1

        if sexo == 'M':
            homens += 1

        if sexo == 'F':
            if idade <= 20:
                mulheres += 1
    elif continuar == 'N':
        print(f'{pessoas_de_maior} cadastros tem mais de 18 anos.')
        print(f'{homens} cadastros são do sexo Masculino.')
        print(f'{mulheres} cadastros são do sexo Feminino e tem Menos de 20 anos.')
        break

print('Fim do Programa')