#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Informe um número: '))
qtde = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[0;33m', c, end=' ')
        qtde += 1
    else:
        print(f'\033[0;31m', c, end=' ')
print(f'\n\033[0;30mO número {n} pode ser dividido {qtde}x.')
if qtde <= 2:
    print(f'Por isso ele é um número primo')
else:
    print(f'Não é um número primo')
