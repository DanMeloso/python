#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
print('===== DESAFIO 6 =====')
enter = input('Digite Algo')

print('É Alfanumerico: ', enter.isalnum())
print('É letra: ', enter.isalpha())
print('É Decimal: ', enter.isdecimal())
print('É Digito????: ', enter.isdigit()) #parecido com inteiro
print('É Identifier ', enter.isidentifier()) # Não possui nenhum caractere especial
print('É minusculo: ', enter.islower())
print('É numerico: ', enter.isnumeric())
print('É impresso?: ', enter.isprintable()) #se todos os caracteres serão visualizados na impressão. incluindo caracteres especiais para criar espaços e quebras de linha
print('É espaço: ', enter.isspace()) #se é somente um espaço
print('É titulo: ', enter.istitle()) #Primeiras Letras Em Maiúsculo Em Cada Palavra
print('É maiusculo: ', enter.isupper())


