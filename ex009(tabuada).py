valor= int(input('Digite o número que deseja saber a tabuada: '))

print('_'* 12)
tabuada= 0
for i in range (10):
    i += 1
    tabuada = valor * i


    print(f'{valor} X {i} = {tabuada}')

print('_'* 12)