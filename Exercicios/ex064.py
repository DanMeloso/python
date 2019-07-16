#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = 0
qtde = 0
n = int(input('Digite um número: '))
while not n == 999:
    soma += n
    qtde += 1
    n = int(input('Digite um número: '))
print('FIM')
print(f'Você digitou {qtde} números, e a soma deles é {soma}')
