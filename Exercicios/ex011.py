#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print('='*5, 'EXERCÍCIO 11', '='*5)
lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = (alt*lar)
tinta = (area/2)
print(f'A área da parede é de {area}m² \nA quantidade de tinta necessária para pintá-la inteira é de {tinta} litros de tinta')
