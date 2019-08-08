#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = list()
menor = ''
maior = ''
for p in range(0, 5):
    lista.append(int(input(f'Digite o valor para a posição {p} :')))

    if menor == '':
        menor = lista[p]
    else:
        menor = min(menor, lista[p])

    if maior == '':
        maior = lista[p]
    else:
        maior = max(maior, lista[p])

print(lista)
print(f'O maior valor foi {maior} e esta nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {menor} e esta nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
