#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um número para que seja calculado o seu fatorial: '))
fatorial = 1
while n > 1:
    print(f'{n} x', end=' ')
    fatorial = fatorial * n
    n -= 1
print(f'1 = {fatorial}')
