#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
print('='*5, 'EXERCÍCIO 24', '='*5)
cidade = str(input('Digite o nome da cidade: ')).strip()
cidade = cidade.lower()
print(f'Nome digitado começa com a palavra Santo? ', {'santo' in cidade.split()[0]})