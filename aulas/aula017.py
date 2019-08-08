#LISTAS
lanche = ['lanche', 'suco', 'pizza', 'pudim']
print(lanche)
#diferente das tuplas, podemos alterar os valores de uma lista
lanche[3] = 'picolé'
print(lanche)
#podemos adicionar outros elementos novos na lista (final da lista)
lanche.append('bolacha')
print(lanche)
#podemos inserir elementos na posição que desejar
lanche.insert(0, 'cachorro quente')
print(lanche)
#apagar elementos
del lanche[3] #remove o elemento na posição 3
print(lanche)
#assim como no caso acima, podemos usar o pop para remover um elemento na lista e passar por parametro a sua posição
#mas é usado geralmente para apagar o ultimo elemento da lista
lanche.pop()
print(lanche)
#podemos tambem remover usando o conteudo da lista, e não o seu indice
lanche.remove('suco')
print(lanche)
#caso tente excluir um elemento que não esteja na lista, a linguagem ira retornar um erro
#a forma correta de excluir um elemento é primeiro fazendo uma verificação
if 'suco' in lanche:
    lanche.remove('suco')
else:
    print('Não existe suco em seu lanche')

valores= [8, 2, 5, 4, 9, 3, 0]
valores.sort() #ordenação dos elementos
valores.sort(reverse=True) #ordenação em ordem inversa
len(valores) #quantidade de elementos

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
