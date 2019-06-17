#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('='*5, 'EXERCÍCIO 25', '='*5)
nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Existe a palavra SILVA em seu nome? ', {'silva' in nome.lower()})
