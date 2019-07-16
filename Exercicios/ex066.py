#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = qtde = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    qtde += 1
print(f'Você digitou {qtde} e a soma é {soma}')
