#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
#de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
anoAtual = date.today().year
nascimento = int(input('Informe o ano de nascimento: '))
idade = anoAtual - nascimento

if idade >= 25:
    print(f'Idade: {idade}.\nCategoria: MASTER')
elif idade >= 19:
    print(f'Idade: {idade}.\nCategoria: SÊNIOR')
elif idade >= 14:
    print(f'Idade: {idade}.\nCategoria: JÚNIOR')
elif idade >= 9:
    print(f'Idade: {idade}.\nCategoria: INFANTIL')
else:
    print(f'Idade: {idade}.\nCategoria: MIRIN')