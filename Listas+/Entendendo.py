# Aula passada
dados = list()
dados.append('Pedro')
dados.append(22)

dados1 = list()
dados1.append('Maria')
dados1.append(21)
# print(dados[0])
# print(dados[1])

# Novo conteúdo:
# pessoas = list()
# pessoas.append(dados[:])
# pessoas.append(dados1[:])
# print(pessoas)
# É possivel adicionar uma lista dentrou de outra lista que será contado como a prmeira lista na posição 0, e assim por diante.
# Também é possivel ser feito de outra maneira:
pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
# que também pode ser chamado de listas compostas

print(pessoas[0][0])
# nesta opção voce estará chamndo de dentro da lista pessoas a lista 0 que contem o elemento chamdo pedro que é o item 0 da lista 0
# Exemplo 2
print(pessoas[1][1])
# Será acessada a lista onde esta presente o nome maria e sera puxado o numero 19 que está presente na posição 1
print(pessoas[1])
# Será apresentado a lista presente na posição 1 que é ['maria', 19]