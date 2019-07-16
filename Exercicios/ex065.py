#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = 0
qtde = 0
maior = menor = 0
primeiraVez = True
contunuar = True
while contunuar:
    n = int(input('Digite um número: '))
    if primeiraVez:
        maior = n
        menor = n
    else:
        maior = max(maior, n)
        menor = min(menor, n)
    soma += n
    qtde += 1
    op = input('Deseja continuar? [S/N]').upper()
    if op == 'N':
        contunuar = False
    primeiraVez = False
print(f'Você digitou {qtde} números. {soma / qtde}')
print(f'Sendo o menor {menor} e o maior {maior}')
