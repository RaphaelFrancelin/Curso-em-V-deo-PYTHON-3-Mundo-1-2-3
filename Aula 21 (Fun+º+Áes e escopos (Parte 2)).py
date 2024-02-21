help(input)#mostra de um jeito interativo as funcionalidade do input, em caso de duvida, só chama o help()
print(input.__doc__)
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função copiada do Gustavo Guanabara do curso em video
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')
help(contador)

#PARAMATROS OPCIONAIS
def somar(a=0, b=0, c=0):#montando a função nesse formato
    # quando a função não recebe um dos valores, o programa intende que vale zero
    s= a+b+c
    print(f'A soma vale {s}')
somar(2,3,5)
somar(7,1)#não coloquei o valor de "c" e mesmo assim o programa é executado, pois é intendido que o valor é zero


#ESCOPO VARIAVEIS
#foi ensinado sobre escopo global e escopo variavel


#USANDO O RETURN
print('Usando o return')
def somar1(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar1(3,2,5)
r2 = somar1(2,6)
r3 = somar1(9)
print(f'As somas dos valores é igual {r1, r2, r3}')
print(f'As somas dos valores é igual {r1}, {r2} e {r3}')
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Digite um número para saber qual valor fatorial: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

def par (n2=0):
    if n2 % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número para saber se é par ou impar: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')



