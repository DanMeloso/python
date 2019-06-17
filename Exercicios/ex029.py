#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('='*5, 'EXERCÍCIO 29', '='*5)
velocidade = float(input('Velocidade do carro: '))
if velocidade > 80:
    excedente = velocidade - 80
    multa = excedente * 7
    print(f'Vá com calma garotão!\nVocê passou à {velocidade}km/m\nTome aqui sua multa R${multa:.2f}')
else:
    print('Ta suave!')