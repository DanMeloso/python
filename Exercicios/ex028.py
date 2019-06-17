#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
print('='*5, 'EXERCÍCIO 28', '='*5)
rand = random.randint(0, 5)
numero = int(input('Eu gerei um número entre 0 e 5. Você pode advinhar? '))
if rand == numero:
    print(f'Uau! Você acertou!\nNúmero {rand}')
else:
    print(f'Que pena pra você. Dessa vez eu venci.\nEu tinha pensando no número {rand}')
print('--FIM--')
