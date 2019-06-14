print('='*5, 'EXERCICIO 10', '='*5)
r = float(input('Digite o valor em reais. R$'))
valDolar = 3.91
d = r//valDolar
resto = r % valDolar
print(f'Com R${r:.2f}, você pode comprar US${d:.2f}')
print(f'Sobram R${resto:.2f}')
