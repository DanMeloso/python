#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
#programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
numero = int(input('Digite o valor de saque - R$'))

qtde50 = numero // 50
resto = numero % 50

qtde20 = resto // 20
resto = resto % 20

qtde10 = resto // 10
resto = resto % 10

qtde1 = resto // 1
resto = resto % 1