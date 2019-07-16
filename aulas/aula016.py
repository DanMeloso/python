#TUPLAS
#podemos inserir mais de uma informação em uma tupla, por exemplo
# lanche = (hamburger, suco, pizza, pudim)
# AS TUPLAS são IMUTÁVEIS. ou seja, não é possível realizar nenhuma alteração em seus itens, ex:
# não posso alterar o pudim por um sorvete

#lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
          #     0          1       2        3

#print(lanche) #imprime toda a tupla
#print(lanche[1]) #imprime o elemento na posição 1
#print(lanche[1:3]) #imprime do elemento 1 ao 2 (ultimo sempre ignorado)
#print(lanche[-2]) #imprime o (ultimo - 2)
#print(lanche[2:]) #imprime do 2 em diante
#print((lanche[:2])) #imprime do inicio até o 2 (ultimo sempre ignorado)

# lanche[1] = 'Refrigerante' ----- TUPLAS SÃO IMUTAVEIS, DARÁ ERRO
#for comida in lanche:
#    print(f'Eu vou comer {comida}')# imprime todos os itens

#print(len(lanche)) #retorna o tamanho da Tupla

#for cont in range(0, len(lanche)):
#    print(lanche[cont])

#for pos, comida in enumerate(lanche):
#    print(f'Comida {comida} na posição {pos}')

#print(sorted(lanche))#imprime organizado

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c) #une as duas duplas

print(c.count(5)) #Quantas vezes aparece o número 5 na tupla
print(c.index(8)) #Em que poisção está o número 8
print(c.index(2)) #Sempre traz a primeira vez que o número aparece na tupla

pessoa = ('Daniel', 28, 'M', 1.79) #podemos unir tipos diferentes
print(pessoa)

del(pessoa) #exclui a tupla inteira, não é possível excluir um único elemento da tupla;
