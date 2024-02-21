numero1 = int(input('Digite o primeiro Número: '))
numero2 = int(input('Digite o segundo Número: '))
numero3 = int(input('Digite o terceiro Número: '))

#Analisando o maior
if numero1 > numero2 and numero1 > numero3:
    print(f'O número {numero1} é maior que número {numero2} e o número {numero3}')
if numero2 > numero1 and numero2 > numero3:
    print(f'O número {numero2} é maior que número {numero1} e o número {numero3}')
if numero3 > numero1 and numero3 > numero2:
    print(f'O número {numero3} é maior que número {numero1} e o número {numero2}')

#Analisando o menor
if numero1 < numero2 and numero1 < numero3:
    print(f'O número {numero1} é menor que número {numero2} e o número {numero3}')
if numero2 < numero1 and numero2 < numero3:
    print(f'O número {numero2} é menor que número {numero1} e o número {numero3}')
if numero3 < numero1 and numero3 < numero2:
    print(f'O número {numero3} é menor que número {numero1} e o número {numero2}')
