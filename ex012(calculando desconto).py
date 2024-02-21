preco= float(input('Digite o Preço do produto: '))
desconto= float(input('Digite % do Desconto: '))

porcentagemDesconto= desconto / 100

valorDoDesconto= preco * porcentagemDesconto

print(f'Preço com Desconto é {preco-valorDoDesconto:.2f}R$')
