#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('='*5, 'EXERCÍCIO 30', '='*5)
numero = int(input('Digite um número e descubra se ele é par ou ímpar'))
r = (numero % 2)
if r == 0:
    print(f'{numero} é PAR')
else:
    print(f'{numero} é ÍMPAR')
print('-- FIM --')
