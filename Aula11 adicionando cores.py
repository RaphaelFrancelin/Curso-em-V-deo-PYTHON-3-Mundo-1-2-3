#ANSI escape sequence

#STYLE 0(None), 1(Bold, negrito), 4(Underline), 7(negative)

#TEXT 30 branco, 31 vermlho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 azul claro, 37 cinza
#BACK(cor de fundo) 40 branco, 41 vermlho, 42 verde, 43 amarelo, 44 azul, 45 roxo, 46 azul claro, 47 cinza

#primeiro codigo do STYLE, agora codigo do TEXT, e agora o codigo do BACK

print('\033[0:30:41mTESTE\033[m')
print('\033[4:33:44mTESTE\033[m')
print('\033[1:35:43mTESTE\033[m')
print('\033[30:42mTESTE\033[m')
print('\033[mTESTE\033[m')
print('\033[7:30mTESTE\033[m')

A=3
B=5
print(f'Os valores são \033[32m{A}\033[m e \033[31m{B}\033[m!!!')

fecharCores ='\033[m'
azul = '\033[34m'
amarelo = '\033[33m'
pretoEbranco = '\033[7:30m'

print(f'{pretoEbranco} Raphael {fecharCores}')
