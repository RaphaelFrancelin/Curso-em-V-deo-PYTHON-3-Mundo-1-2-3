salario = float(input('Qual o seu salário? R$'))

if salario > 1250.00:
    aumento = salario * (10/100) + salario
else:
    aumento = salario * (15/100) + salario

print(f'O seu salário era R${salario:.2f} agora é R${aumento:.2f}')