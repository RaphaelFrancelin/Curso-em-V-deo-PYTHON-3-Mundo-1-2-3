import datetime
dataAtual = datetime.date.today().year


numeroDaPessoa = 1
contadorDeMaioridade = 0
contadorDeMenoridade = 0

for pessoas in range (1,8):
    primeiraPessoa = int(input(f'Qual ano que a {numeroDaPessoa}ª Pessoa nasceu? '))
    verificacaoIdade = dataAtual - primeiraPessoa
    numeroDaPessoa += 1
    if verificacaoIdade >= 21:
        contadorDeMaioridade += 1
    else:
        contadorDeMenoridade += 1
print(f'Temos {contadorDeMaioridade} de Maioridade e temos {contadorDeMenoridade} de Menoridade.')
