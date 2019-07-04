#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from time import sleep
maior = 0
menor = 0
pessoas = int(input('Informe a quantidade de pessoas que deseja analisar: '))
for c in range(0, pessoas):
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Analisando a idade das {pessoas} informadas.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
print(f'Temos {menor} pessoas MENORES DE IDADE')
print(f'Temos {maior} pessoas MAIORES DE IDADE')
