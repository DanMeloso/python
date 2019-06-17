#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
print('='*5, 'EXERCÍCIO 20', '='*5)
n1 = 'Daniel'
n2 = 'Monique'
n3 = 'Tadeu'
n4 = 'Miran'
lista = [n1, n2, n3, n4]
t = random.sample(lista, 4)
print(f'A ordem de apresentação será {t}')
