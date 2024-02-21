frase='   Curso em Vídeo Python             '
print(frase[3])
print (frase[3:13])
print (frase[:13])
print (frase[13:])
print (frase[1:15])
print (frase[1:15:2])
print (frase[1::2])

print(frase.count('o'))
print(frase.upper().count('o'))#conta quantos letras 'o' jogada para Maiuscula tem em frases

print(len(frase)) #se adicionar espaços aumenta o tamanho do lenght

print(len(frase.strip())) # remove excesso de espaços antes e depois da string

print(frase.replace('Python', 'Android'))# é trocado somente nessa instância se for
# necessário substituir use frase= frase.replace('Python', 'Android')

print('Curso' in frase)
print(frase.find('Vídeo'))#mostra a posição
print(frase.find('vídeo'))#não mostra por estar tudo minusculo
print(frase.lower().find('vídeo'))#a frase foi passado para minusculo e depois procurou a palavra vídeo

print(frase.split())#Dividiu a frase e transformou em uma lista
dividido= frase.split()
print(dividido[0])
print(dividido[1])
print(dividido[2][3])# terceira letra da sengunda palavra