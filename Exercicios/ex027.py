#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.
print('='*5, 'EXERCÍCIO 27', '='*5)
nome = str(input('Digite seu nome completo: '))
nomeSplit = nome.split()
ultimoIndice = (len(nome.split()))
print(f'O primeiro nome é {nomeSplit[0]} e o último nome é {nomeSplit[ultimoIndice-1]}')
