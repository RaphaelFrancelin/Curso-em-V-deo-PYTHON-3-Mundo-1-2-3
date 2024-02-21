diaAluguel= float(input('Quantos dias precisa? '))
kmRodado= float(input('Quantos Kilômetros rodados? '))

valorDiaAluguel= diaAluguel * 60

valorKmRodado= kmRodado * 0.15

totalPagar= valorKmRodado + valorDiaAluguel

print(f'O valor total a pagar é {totalPagar:.2f}R$')