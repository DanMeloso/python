print('='*5, 'EXERCÍCIO 7', '=*5')
nome = str(input('Nome do aluno: '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
med = (n1 + n2) / 2
print(f'A média do aluno {nome} é {med:.2f}')
if med >= 6:
    print(f'{nome} está APROVADO')
else:
    print(f'{nome} está REPROVADO')
