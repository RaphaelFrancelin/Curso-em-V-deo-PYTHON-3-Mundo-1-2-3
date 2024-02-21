sexo = str(input('Inform seu sexo: [F/M] ')).upper().strip()[0]#foi feito um fatiamento somente para pegar a primeira letra.
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')