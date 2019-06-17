#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
print('='*5, 'EXERCÍCIO 22', '='*5)
nome = str(input('Digite seu nome completo'))
#nome = 'Daniel Guilherme Meloso'

print(f'Nome com todas as letras em maiúsculo: {nome.upper()}')
print(f'Nome com todas as letras em minúsculo: {nome.lower()}')

aux = (nome.split())
nomeSemEspaco = ''.join(aux)
print(f'{nome} sem espaços fica {nomeSemEspaco} e possui {len(nomeSemEspaco)} letras')

print(f'{aux[0]} tem {len(aux[0])} letras')

