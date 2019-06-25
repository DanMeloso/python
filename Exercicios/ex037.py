#Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para BINÁRIO
# 2 para OCTAL
# 3 para HEXADECIMAL

numero = int(input('Informe um número: '))
op = int(input('DIGITE\n1 para Binário\n2 para Octal\n3 para Hexadecimal '))
if op == 1:
    print(f'O número {numero} em Binário é: ')
elif op == 2:
    print(f'O número {numero} em Octal é: ')
elif op == 3:
    print(f'O número {numero} em Hexadecimal é: ')
else:
    print('Opção de conversão inválida')