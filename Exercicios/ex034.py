#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('='*5, 'EXERCÍCIO 34', '='*5)
salario = float(input('Digite o salário atual R$'))
if salario >1250:
    salario = salario + (salario * 10) / 100
else:
    salario = salario + (salario * 15) / 100
print(f'Novo salário R${salario}')