#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('='*5, 'EXERCÍCIO 31', '='*5)
distancia = float(input('Informe a distância da viagem: '))
if distancia > 200:
    valor = distancia * 0.45
    print('Valor por KM = R$0,45')
    print(f'Para uma viagem de {distancia}Km, o valor será R${valor:.2f}')
else:
    valor = distancia * 0.50
    print('Valor por KM = R$0,50')
    print(f'Para uma viagem de {distancia}Km, o valor será R${valor:.2f}')
print('Boa Viagem!')
