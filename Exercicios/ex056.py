#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
med = 0
nomeMaisvelho = ''
idadeMaisVelho = 0
qtdeMulheres20 = 0
for p in range(1, 4+1):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: '))

    med += i

    if s in 'Mm':
        if p == 1:
            nomeMaisvelho = nome
            idadeMaisVelho = i
        else:
            if i > idadeMaisVelho:
                nomeMaisvelho = nome
                idadeMaisVelho = i
    else:
        if i < 20:
            qtdeMulheres20 += 1
print(f'Média de idade do grupo de pessoas: {med/4}')
print(f'O homem mais velho é o {nomeMaisvelho} com {idadeMaisVelho} anos')
print(f'Quantidade de mulheres menores de idade: {qtdeMulheres20}')
