#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print('='*5, 'EXERCÍCIO 32', '='*5)
ano = int(input('Digite um ano e descubra se é um ano bisexto: '))
bissexto = ano % 4
if bissexto == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')
