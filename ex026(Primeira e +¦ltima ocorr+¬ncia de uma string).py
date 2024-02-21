frase = str(input('Digite uma frase: ')).strip().upper()

print(f'Essa frase tem {frase.count("A")} letra(s) A.')

print(frase.find('A')+1)

print(frase.rfind('A')+1)
