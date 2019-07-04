#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = str(input('Informe o seu sexo: [M/F]'))
while s not in 'Mm' and s not in 'Ff':
    s = str(input('Informe o seu sexo: [M/F]'))
    if s not in 'Mm' and s not in 'Ff':
        print('Dados inválidos')
if s in 'Mm':
    print('Masculino')
else:
    print('Feminino')
