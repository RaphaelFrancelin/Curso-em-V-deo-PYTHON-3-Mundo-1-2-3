texto = str(input('Digite seu texto: ')).strip().upper()

semEspaco = texto.replace(' ','')

inverso = ''# é possível usar a tecnica de fatiamento que ficaria assim
            #inverso = semEspaco [::-1] nesse exemplo não precisa usar laço for
for letra in range ( len(semEspaco) - 1, -1, -1):
    inverso += semEspaco[letra]
print(f'A frase digitada é {semEspaco} e o inverso é {inverso}')

if inverso == semEspaco:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é palindromo')
