#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
r1 = float(input('Informe o PRIMEIRO SEGMENTO: '))
r2 = float(input('Informe o SEGUNDO SEGMENTO: '))
r3 = float(input('Informe o TERCEIRO SEGMENTO: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos informados PODEM formar um Triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos informados NÃO PODEM formar um triângulo')