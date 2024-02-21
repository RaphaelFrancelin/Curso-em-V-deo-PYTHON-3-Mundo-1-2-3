salario= float(input('Digite o salário: '))
aumento= float(input('Digite a porcentagem do Aumento: '))

porcentagemAumento= aumento / 100

valorDoAumento= salario * porcentagemAumento

print(f'Seu salário que era {salario}R$ agora com aumento de {aumento} % seu salário passa a receber {salario+valorDoAumento:.2f}R$')