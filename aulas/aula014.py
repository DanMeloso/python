#While - Estrutura de repetição com teste lógico
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

#Usando o FOR quando sabemos o limite
#podemos usar o WHILE para quando soubermos o limite
#mas, SÓ PODEMOS USAR O WHILE QUANDO NÃO SABEMOS O LIMITE
#ou seja, que precise repetir até alguma condição ser atentida.

n = 1
pares = impares = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'Você digitou {pares} números pares e {impares} números ímpares')
print('FIM')

