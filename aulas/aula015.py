soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma dos valores digitados é {soma}')

#podemos criar um loop infinito e, para sair do mesmo, utilizamos o comando BREAK
#sairá do loop.