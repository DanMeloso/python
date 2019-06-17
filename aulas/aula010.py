#tempo = int(input('Quantos anos tem seu carro?'))
#if tempo <=3:
#    print('Carro novo')
#else:
#    print('Carro velho')
#print('--FIM--')
#
# ou #
#print('carro novo' if tempo<=3 else 'carro velho')

##########################################################################
import emoji
nome = str(input('Qual é o seu nome?')).strip().lower()
if nome == 'daniel':
    print(emoji.emojize('Que nome lindo você tem :heart_eyes:', use_aliases=True))
else:
    print(emoji.emojize('Seu nome é tão tão normal :disappointed:', use_aliases=True))
print(f'Bom dia, {nome}')

###########################################################################
n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.2f}')
if m >= 6:
    print('Sua média foi boa! Parabens')
else:
    print('Sua média foi ruim! Estude mais')
