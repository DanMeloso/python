#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
print('='*5, 'EXERCÍCIO 18', '='*5)
angulo = float(input('Digite a área do angulo'))
print(f'Seno: {math.sin(math.radians(angulo))}')
print(f'Coseno: {math.acos(math.radians(angulo))}')
print(f'Tangente: {math.tan(math.radians(angulo))}')