nome = str(input('Digite seu Nome: ')).strip()

print(f'Seu nome em Letras Maiúsculas {nome.upper()}.')

print(f'Seu nome em Letras Minúsculas {nome.lower()}.')

semEspaco = nome.replace(' ', '')
print(f'Seu nome tem {len(semEspaco)} letras.')

dividindo = nome.split()
primeiroNome = dividindo[0]
print(f'Seu primeiro nome tem {len(primeiroNome)} letras.')
