#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase'))
frase = frase.upper().replace(' ', '')
invert = ''
invert = frase[::-1]
'''for c in range(len(frase), 0, -1):
    invert = invert + frase[c-1]'''

print(f'A frase {frase} invertida é {invert}')
if frase == invert:
    print('Temos um palíndromo')
else:
    print('NÃO temos um palíndromo')



