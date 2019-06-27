#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoAtual = (int(date.today().year))
nascimento = int(input('Informe o ano de nascimento: '))
idade = anoAtual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos.')
if idade == 18:
    print(f'Aliste-se IMEDIATAMENTE')
elif idade > 18:
    print(f'Seu alistamento foi há {idade-18}')
    print(f'Você deveria ter se alistado no ano de {anoAtual - (idade-18)}')
else:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento')
    print(f'Seu alistamento será em {anoAtual + (18 - idade)}')
