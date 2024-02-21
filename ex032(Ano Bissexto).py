import  datetime

ano = int(input('Digite o ano para saber se é Bissexto se quiser o ano atual digite 0: '))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:# ano divisivel por 4 e sobra 0 é bissexto,
    # mas os que são divisiveis por 100 ou 400 for diferente de 0 não são Bissexto
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')
