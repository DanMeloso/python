#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    cont = 1
    n = int(input('Deseja visualizar a tabuada de qual número? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    print('-' * 30)
print('Obrigado por utilizar a tabuada 3.0 - Volte sempre!')