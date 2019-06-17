#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
print('='*5, 'EXERCÍCIO 17', '='*5)
import math
catOposto = float(input('Informe o valor do cateto oposto: '))
catAdja = float(input('Informe o valor do cateto adjacente: '))
hip = math.hypot(catOposto, catAdja)
print(f'O valor do comprimeiro da hipotenusa é {hip:.2f}')
