#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print('='*5, 'EXERCÍCIO 13', '='*5)
salario = float(input('Informe o salário do funcionário R$'))
percentual = float(input('Informe o percentual de aumento do funcionário: '))
novoSalario = salario + ((salario*percentual)/100)
print(f'Salário atual R${salario:.2f}')
print(f'Salário com {percentual:.2f}% de aumento R${novoSalario:.2f}')
