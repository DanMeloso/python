#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('='*5, 'EXERCÍCIO 15', '='*5)
km = float(input('Informe a quantidade de KM"s percorridos: '))
dias = int(input('Informe a quantidade de dias que o carro foi alugado: '))
valor = (dias*60) + (km*0.15)
print('-'*25)
print(f'O carro foi alugado por {dias} dias e rodou {km}km"s')
print(f'Valor do aluguel = {dias} x R$60,00 --> R${dias*60:.2f}')
print(f'Valor da quilometragem = {km}Km"s x R$0,15 --> R${km*0.15:.2f}')
print('-'*25)
print(f'Valor total a pagar R${valor:.2f}')
