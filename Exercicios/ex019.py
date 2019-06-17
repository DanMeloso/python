#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
print('='*5, 'EXERCÍCIO 19', '='*5)
nome1 = str(input('Primeiro Nome: '))
nome2 = str(input('Segundo Nome: '))
nome3 = str(input('Terceiro Nome: '))
nome4 = str(input('Quarto Nome: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')

