#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
op = 0
while not op == 5:
    print('-='*15)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    print('-=' * 15)
    op = int(input('Opção: '))

    if op in [1, 2, 3, 4, 5]:
        if op == 1:
            print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        elif op == 2:
            print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
        elif op == 3:
            print(f'O maior número entre {n1} e {n2} é o {max(n1, n2)}')
        elif op == 4:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
        elif op == 5:
            print('Encerrando', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
    else:
        print('\nOpção Inválida. Digite novamente')
print('Obrigado, volte sempre!')
