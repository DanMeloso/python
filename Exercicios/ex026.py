#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
#aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
print('='*5, 'EXERCÍCIO 26', '='*5)
frase = 'Essa aqui é a minha frase de exemplo, vamos ver quantas letras "a" temos nela.'
frase = frase.strip()

print(f'Nesta frase, existem ', frase.lower().count('a'), 'vezes a letra "a"')
print(f'A primeira vez que a letra "a" aparece é na posição:', frase.lower().find('a')+1)
print(f'A ultima vez que a letra "a" aparece é na posição:', frase.lower().rfind('a')+1)
