#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('''ESCOLHA SUAS ARMAS:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*15)
print(f'O computador escolheu', itens[pc])
print(f'O jogador escolheu', itens[op])
print('-='*15)
if pc == 0:# Computador escolheu PEDRA
    if op == 0:
        print('EMPATE')
    elif op == 1:
        print('JOGADOR VENCEU')
    elif op == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Opção INVÁLIDA!')
elif pc == 1:#Computador escolheu PAPEL
    if op == 0:
        print('COMPUTADOR VENCEU')
    elif op == 1:
        print('EMPATE')
    elif op == 2:
        print('JOGADOR VENCEU')
    else:
        print('Opção INVÁLIDA!')
else:#Computador escolheu TESOURA
    if op == 0:
        print('JOGADOR VENCEU')
    elif op == 1:
        print('COMPUTADOR VENCEU')
    elif op == 2:
        print('EMPATE')
    else:
        print('Opção INVÁLIDA!')
