#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a Razão'))
numero = 0
c = 0
while c < 10:
    if c == 0:
        numero = termo
    else:
        numero = numero + razao
    c += 1
    print(numero, end=' → ')
print('FIM')
