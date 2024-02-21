sexo = str(input('Digite sexo: [F/M] ')).upper().strip()
while sexo != 'F' or sexo != 'M':
    print('Valor inválido, por favor digite M para masculino ou F para feminino: ')
    sexo = str(input('Digite sexo: [F/M] ')).upper().strip()
    if sexo == 'F':
        print(f'Sexo {sexo} Feminino restridado com sucesso.')
        exit()
    if sexo == 'M':
        print(f'Sexo {sexo} Masculino restridado com sucesso.')
        exit()
