#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print('='*5, 'EXERCÍCIO 12', '='*5)
precoProduto = float(input('Digite o valor do produto R$'))
percentualDesconto = float(input('Informe o percentual de desconto: '))
precoComDesconto = (precoProduto * percentualDesconto) / 100
print('-'*25)
print(f'Valor do produto R${precoProduto:.2f}')
print(f'Percentual de desconto {percentualDesconto:.2f}%')
print(f'Valor do Desconto R${precoComDesconto:.2f}')
print('-'*25)
print(f'Valor do produto com Desconto R${(precoProduto - precoComDesconto):.2f}')
