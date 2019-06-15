#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
print('='*5, 'EXERCÍCIO 14', '='*5)
c = float(input('Informe a temperatura em ºC'))
f = ((9 * c) / 5) + 32
print(f'A temperatura de {c}ºC equivale a {f}F')

