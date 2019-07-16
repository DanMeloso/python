#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
#de uma Sequência de Fibonacci.
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
qtdeTermos = int(input('Quantos termos deseja visualizar? '))
t1 = 0
t2 = 1
print('~'*30)
print('0 → 1', end=' → ')
cont = 2
while cont < qtdeTermos:
    t3 = t1 + t2
    print(t3, end=' → ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')