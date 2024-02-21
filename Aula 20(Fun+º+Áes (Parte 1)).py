print('-'*30)
print('  CURSO EM VIDEO  ')
print('-'*30)
print('-'*30)
print('  APRENDA PYTHON')
print('-'*30)
print('-'*30)
print('  GUSTAVO GUANABARA  ')
print('-'*30)


#PROGRAMA PRINCIPAL
print('ROTINA! (def)')


def lin():
    print('-' * 30)


lin()
print('  CURSO EM VIDEO  ')
lin()
lin()
print('  APRENDA PYTHON')
lin()
lin()
print('  GUSTAVO GUANABARA  ')
lin()

lin()
#PROGRAMA PRINCIPAL 1
print('ROTINA! (def1)')


def título(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


título('  CURSO EM VIDEO  ')
título('  APRENDA PYTHON')
título('  GUSTAVO GUANABARA  ')
lin()
print('ROTINA! (def1)')


def soma(a, b):
    s= a + b
    print(f'A soma A= {a} e B= {b} é igual à {s}')


#PROGRAMA PRINCIPAL, se receber um valor a mais ele não vai entender, pois, está definido que irá receber apenas A e B
#isso é chamado de empacotamento
soma(4, 5)
soma(8, 9)
soma(2, 1)
lin()
#Temos essa forma de gerar um desempacotamento, quando precisamos receber e não sabemos quantos iremos receber
def soma1(*valores1):
    s = 0
    for num in valores1:
        s+= num
    print(f'Somando os valores do desempacotamento {valores1} temos {s}')


soma1(5, 2)
soma1(2, 9, 4)

lin()
#DEFINIÇÃO RECEBENDO UMA LISTA, aqui estamos criando uma definição que dobras todos os valores gerados
#para que isso aconteça temos que usar lista por que são mutaveis


def dobra(lista):
    pos= 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores= [6, 3, 9, 1, 0, 2]#atenção que aqui é uma lista [] se usarmos () ele vira uma tupla e tuplas não são mutaveis
dobra(valores)
print(f'Os valores dobrados são {valores}')
lin()