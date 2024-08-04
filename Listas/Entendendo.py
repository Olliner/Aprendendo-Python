lanche = ['Hamburguer', 'Suco', 'Pizza','Pudim']
lanche[3]= 'Picole'
lanche.append('cookie')
lanche.insert(0,'Cachorro-Quente')
del lanche[3] #Apaga a pizza
# Método de verificar se a um elemento na lista:
if 'Pizza' in lanche:
    lanche.remove('Pizza')
print(lanche)

# Listas sõa Mutaveis
#Tuplas não sõa mutaveis

# Método append para dicionar elementos: (Adicionado ao final da lista)
# Método insert: Com ele voce pode adicionar um elemento em qualquer posição da lista:
# Eliminação de elementos: 'Del', 'pop', 'remove': Método pop normalmente utilizado para apagar o ultimo elemento porem é possivel passar o indece Ex: lanche.pop[3] ou lanche.pop():Método remove apaga pelo conteudo dentro da lista exemplo:lanche.remove('Pizza') o remove so exclui a primeira ocorrencia do elemento

# Criação de listas através de range:
valores = list(range(4, 11))
print(valores)

#Colocando elementos em ordem:
valores1 = [8,2,5,4,9,3,0]
valores1.sort()
print(valores1)
#colocando em ordem contrária
valores1.sort(reverse=True)
print(valores1)
#Saber o tamnho da lista:
print(len(valores1))