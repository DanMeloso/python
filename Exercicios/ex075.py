#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o úmtimo número: '))
numeros = (n1, n2, n3, n4)
print(f'Apareceram {numeros.count(9)}x o número 9')
if 3 in numeros:
    print(f'A primeira vez que foi digitado o número 3, foi na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitador foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
