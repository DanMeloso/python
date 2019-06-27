#Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
res = ''
for c in range(2, 50+1, 2):
    res = res + ' ' + str(c)
print(res)
print('Acabou!')

for c in range(2, 50+1, 2):
    print(c, end=' ')
print('Acabou!')