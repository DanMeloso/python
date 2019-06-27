#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500
num = 0
qtde = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        num += c
        qtde += 1
print(f'A somatória de todos os {qtde} números é {num}')
print('FIM')
