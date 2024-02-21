valorCasa = int(input('Qual valor do Imóvel? '))
salario = float(input('Qual seu salário? '))
prestacoes = int(input('Quantos anos deseja o financiamento? '))

quantidadePrestacoes = prestacoes * 12

valorPrestacoes = valorCasa / quantidadePrestacoes

limitePrestacao = salario * (30/100)

if valorPrestacoes > limitePrestacao:
    print('A prestação do seu imóvel é maior que 30% da sua renda, por isso hoje NÃO aprovamos seu credito')
else:
    print('Credito aprovado')