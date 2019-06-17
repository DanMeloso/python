#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
print('='*5, 'EXERCÍCIO 16', '='*5)
numero = float(input('Digite um número: '))
numeroInteiro = trunc(numero)
print(f'O número digitado foi {numero} e sua parte inteira é {numeroInteiro}')
