#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros
import emoji
print(f'='*15, emoji.emojize(':honeybee: LOJAS MELOSO :sunflower:'), '='*15)
compra = float(input('Preço das compras R$'))
print('     FORMA DE PAGAMENTO')
print('''
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3X ou mais no cartão''')
op = int(input('Informe a opção de pagamento: '))
print('-'*50)
if op == 1:
    valor = compra - (compra * 10 / 100)
    print(f'O valor da compra é R${compra:.2f}\nCom pagamento à vista em Dinheiro/Cheque será R${valor:.2f}')
elif op == 2:
    valor = compra - (compra * 5 / 100)
    print(f'O valor da compra é R${compra:.2f}\nCom pagamento à vista no cartão será R${valor:.2f}')
elif op == 3:
    print(f'O valor da compra é R${compra:.2f}')
    qtde = int(input('Deseja parcelar em quantas vezes? '))
    if qtde > 0 and qtde <= 2:
        print(f'Serão {qtde}x de R${compra / qtde:.2f}')
    else:
        print('Quantidade de parcelas inválida para essa forma de pagamento')
elif op == 4:
    valor = compra + (compra * 20 / 100)
    print(f'O valor da compra é de R${compra:.2f}\nCom pagamento em 3x ou mais o valor será R${valor:.2f}')
    qtde = int(input('Deseja parcelar em quantas vezes? '))
    if qtde >= 3:
        print(f'Serão {qtde}x de R${valor / qtde:.2f}')
    else:
        print('Quantidade de parcelas inválida para essa forma de pagamento')
print('-'*50)
