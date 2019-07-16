#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
eighteenPlus = 0
homens = 0
mulheres20 = 0
pessoas = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = (input('Sexo [M/F]')).upper().strip()[0]
    while not sexo in ('MF'):
        sexo = (input('Sexo [M/F]')).upper().strip()[0]

    if idade >= 18:
        eighteenPlus += 1

    if sexo in ('Mm'):
        homens += 1
    else:
        if idade < 20:
            mulheres20 += 1

    pessoas += 1
    continuar = input('Deseja Continuar? [S/N]').strip().upper()[0]
    while not continuar in ('SN'):
        continuar = input('Deseja Continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {pessoas} pessoas')
print(f'{eighteenPlus} tem mais de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastradas {mulheres20} mulheres com menos de 20 anos')
