#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
rand = random.randint(0, 10)
print('Olá desafiante... Eu pensei em um número, será que consegue adivinhar?')
acertou = False
qtde = 0
while not acertou:
    n = int(input('Digite seu palpite: '))
    qtde += 1
    if n == rand:
        acertou = True
    else:
        if n < rand:
            print('Tente um número MAIOR...')
        else:
            print('Tente um número MENOR')
print('Você me VENCEU', end=' ')
print(f'Com {qtde} tentativas')
print('FIM')
