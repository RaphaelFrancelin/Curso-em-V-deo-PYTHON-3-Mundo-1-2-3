from random import shuffle

aluno1= str(input('Digite o Nome do Primeiro Aluno: '))
aluno2= str(input('Digite o Nome do Segundo Aluno: '))
aluno3= str(input('Digite o Nome do Terceiro Aluno: '))
aluno4= str(input('Digite o Nome do Quarto Aluno: '))

alunos= [aluno1,aluno2, aluno3, aluno4]

ordemAlunos= shuffle(alunos)

print(f'A ordem dos aleatória dos alunos é {alunos}.')