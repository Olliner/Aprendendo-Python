
# dados = {'nome':'Pedro', 'Idade':25}
# print(dados['nome'])
# print(dados['Idade'])

# # como adicionar ao dicionario um elemento
# dados['sexo'] = 'M'
# print(dados)

# # Para remover um elemento
# del dados['Idade']
# print(dados)

filme = {
    'Titulo':'Star Wars',
    'ano': 1977,
    'diretor':'George Lucas'
}
print(filme.values()) #Pega somente os valores atribuidos as keys
print(filme.keys()) #Pega somente as keys
print(filme.items()) #Pega todos os items seprand-os por keys

for k, v in filme.items(): #Para cada key e valor no filme.items
    print(f'O {k} é {v}')