#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
tabela = ('Santos','PALMEIRAS','Flamengo','Atlético-MG','São Paulo','Internacional','Atlético-PR','Cutintia','Goiás',
          'Botafogo','Grêmio','Bahia','Ceará','Fortaleza','Vasco','Cruzeio','Fluminense','Chapecoense','CSA','Avaí')

print(tabela)
print('=-'*120)
print(tabela[0:6])
print('=-'*120)
print(tabela[-4])
print('=-'*120)
print(sorted(tabela))
print('=-'*120)
print(tabela[16:21])
print('=-'*120)
print(f'A Chapecoense está na posição: ', tabela.index('Chapecoense')+1)
print('=-'*120)
