#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
x = 0
for c in range(termo, decimo + razao, razao):
    print(c, end=' →')
print('ACABOU!')

