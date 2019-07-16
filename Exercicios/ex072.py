#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
#de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
          'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 1 e 20: '))
while not (n >= 0 and n < 21):
    n = int(input('Opção Inválida. Digite um número entre 1 e 20: '))
    if n > 0:
        n = n - 1
print(f'Você digitou o número {numero[n]}')