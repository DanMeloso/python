#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for c in range(1, 7):
    n = int(input('Digite um número'))
    if n % 2 == 0:
        soma += n
print(f'A somatória dos números pares digitados foi {soma}')