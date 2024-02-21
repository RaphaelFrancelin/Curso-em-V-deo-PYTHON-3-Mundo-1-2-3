valorVenda = float(input('Valor da Venda: '))
formasPagamento = int(input('Qual será a Forma de pagamento?\n'
                        '[1] À vista dinheiro/pix\n'
                        '[2] À vista no cartão\n'
                        '[3] 2X no cartão\n'
                        '[4] 3x ou mais no cartão\n'
                        'Qual sua opção: '))

if formasPagamento == 1:
    print(f'O valor da sua compra é de {valorVenda - (valorVenda * (10/100))}R$ você teve 10% de desconto.')

elif formasPagamento == 2:
    print(f'O valor da sua compra é de {valorVenda - (valorVenda * (5/100))}R$ você teve 5% de desconto.')

elif formasPagamento == 3:
    print(f'O valor da sua compra é de 2 parcelas de {valorVenda/2}R$.')

elif formasPagamento == 4:
    parcelas = int(input('Quantas parcelas vai fazer: '))
    print(f'O valor da sua compra é de {parcelas} parcelas de {((valorVenda*(20/100))+valorVenda) / parcelas}R$ '
          f'o valor total da sua compra ficará em {((valorVenda*(20/100))+valorVenda)}R$.')
else:
    print('Opção invalida, tente novamente.')

