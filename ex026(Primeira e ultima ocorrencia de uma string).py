frase = str(input('Digite uma frase: ')).strip().upper()

qttdLetrasA= frase.count('A')
print(f'A letra A aparece {qttdLetrasA} vezes na frase.')
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(frase.find('A')+1)
print(frase.rfind('A')+1)