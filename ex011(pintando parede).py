altura= float(input('Qual a altura da parede que deseja pintar (Metros): '))
comprimento= float(input('Qual o comprimento da parede que deseja pintar (Metros): '))
litroDeTinta= float(input('De acordo com o fabricante digite quantos metros quadrado 1 litro de Tinta cobre: '))

area= altura * comprimento


print(f'Você vai usar uma média de {area/litroDeTinta:.2f} Litro(s) de tinta')
