nome = str(input('Digite seu Nome: ')).strip()

print('Muito prazer em te conhecer! ')

separando= nome.split()

print(f'Seu primeiro nome é {separando[0]}.')

print(f'Seu ultimo Nome é {separando[len(separando)-1]}.')#como professor fez no curso

ultimoNome= separando.pop()

print(f'Seu ultimo Nome é {ultimoNome}.')
