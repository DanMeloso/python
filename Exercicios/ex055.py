#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pessoas = int(input('Informe a quantidade de pessoas que deseja analisar: '))
peso = 0
maior = 0
menor = 0
for c in range(0, pessoas):
    peso = float(input('Informe o peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'MAIOR: {maior}')
print(f'MENOR: {menor}')


