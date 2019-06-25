#DESAFIO 36
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valo da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado

print('='*8, 'EXERCÍCIO 36', '='*8)
valorDaCasa = float(input('Informe o valor da casa R$'))
salario = float(input('Informe o seu salário R$'))
anos = int(input('Informe a quantidade de anos que deseja pagar: '))

qtdeParcelas = anos * 12
valorParcela = valorDaCasa / qtdeParcelas
valorLimiteParcela = salario * 30 / 100

if valorLimiteParcela < valorParcela:
    print('INFELIZMENTE não podemos fechar negócio')
    print(f'Para financirar em {anos}, seriam {qtdeParcelas} parcelas de R${valorParcela}')
    print(f'Não podemos comprometer mais que 30% de seu salário que é de R${valorLimiteParcela}')
else:
    print('PODEMOS fazer negócio!')
    print(f'Ficará em {qtdeParcelas} parcelas de R${valorParcela}')


