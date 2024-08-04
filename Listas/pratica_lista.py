# valores = list()

# # Reconhecer valores pelo teclado
# for cont in range(0, 5):
#     valores.append(int(input('digite um valor:')))

# # Este comando Vai me falar onde esta a posição[c] de cada valor
# for c, valor in enumerate(valores):
#     print(f'Na posiçõa {c} encontrei o valor {valor}!')
# print('Cheguei ao final da lista')

a =[2, 3, 4, 7]
# Sempre que linkar uma lista na outra elas estaram sempre ligas
# b = a
# metodo de fazer uma copia de todos os valores
b = a[:]
b[2] = 8
print (f'Lista A: {a}')
print (f'Lista B: {b}')