#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
#vogais = ('a', 'e', 'i', 'o', 'u')
#for n in range(0, len(palavras)):
#    print(f'Na palavra {palavras[n]} temos as seguintes vogais: ', end=' ')
#    for j in range(0, len(palavras[n])):
#        palavra = (palavras[n])
#        print(palavra[j])
#    print(f'\n')

for p in palavras:
    print(f'\nNa palavra {p} temos as seguintes vogais: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
