#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
print('='*5, 'EXERCÍCIO 23', '='*5)
#numero = str(input('Digite um número entre 0 e 9999'))
numero = 1578

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Analisando o número {numero}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
