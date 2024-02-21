from datetime import date

anoNascimento = int(input('Qual seu ano de Nascimento: '))

idade = date.today().year - anoNascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos idade e sua classificação é MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos idade e sua classificação é INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos idade e sua classificação é JÚNIOR.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos idade e sua classificação é SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos idade e sua classificação é MASTER.')