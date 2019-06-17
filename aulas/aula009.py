frase = 'Curso em Video Python'
print(frase)
print(frase.find('Python')) #retorna a posição que inicia a palavra
print('Curso' in frase) #se existe esse caractere na string
print(frase[9]) #retorna o caractere da posição 9
print(frase.count('o')) #retorna a quantidade de vezes que encontrou a letra o
print(frase[:9]) #da posição inicial até a 9
print(frase[9:]) #a partir da posição 9 até o final
print(frase[0:21:2]) #a partir do 0 até 21, pulando de 2 em 2


print(frase.upper())
print(frase.lower())
print(len(frase)) #tamanho
print(frase.capitalize()) #joga todos os caracteres para minusculo e a primeira letra da frase será maiuscula
print(frase.title()) #Primeira letra de cada palavra será maiúscula. Restante minusculo.
print(frase.strip()) #remove os espaços no inicio e do final da string
print(frase.rstrip()) #remove os espaços no final da string.
print(frase.lstrip()) #remove os espaços no inicio da string.

print(frase.split()) #separa todas as palavras em indices de uma nova lista
fraseSplit = frase.split()
print('-'.join(fraseSplit)) #inverso do split
print('-'.join(frase))
dividido = frase.split()
print(dividido[2])