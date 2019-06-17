#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('='*5, 'EXERCÍCIO 33', '='*5)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        maior = n1
    else:
        maior = n3
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3

if n1 < n2:
    if n1 < n3:
        menor = n1
    else:
        menor = n3
else:
    if n2 < n3:
        menor = n2
    else:
        menor = n3
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
