#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
#mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
p = float(input('Digite o seu peso em KG: '))
a = float(input('Digite a sua altura: '))
imc = p / (a**2)
print(f'Seu IMC é de {imc:.2f}')

if imc < 18.5:
    print('Está ABAIXO do peso')
elif imc < 25:
    print('Está com o PESO IDEAL')
elif imc < 30:
    print('Está com SOBREPESO')
elif imc < 40:
    print('Está com OBESIDADE')
else:
    print('Está com OBESIDADE MÓRBIDA')
