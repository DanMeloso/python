#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = maiorMil = 0
maisBarato = ''
menor = 0
produtoMenor = ''
while True:
    produto = str(input('Produto: '))
    preco = float(input('R$ '))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    total += preco

    if preco >= 1000:
        maiorMil += 1

    if menor == 0:
        menor = preco
        produtoMenor = produto
    else:
        if preco < menor:
            menor = preco
            produtoMenor = produto

    if continuar == 'N':
        break

print('{:-^50}'.format('FIM DO PROGRAMA'))
print(f'O valor total de sua compra é de R${total:.2f}')
print(f'{maiorMil} produtos tem o valor maior que R$1.000')
print(f'O produto mais barato de sua compra é: {produtoMenor}')
print('-'*50)
