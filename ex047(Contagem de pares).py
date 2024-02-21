for c in range(2, 51, 2):
    print(c, end=' ')

print('Fim')
print('-='*38)

for c in range(1, 51):  #nesse tipo de programação demora um pouco mais por fazer
                        # mais iterações. Por ter que dividir por todos os numeros
    if c % 2 == 0:
        print(c, end=' ')

print('Fim')