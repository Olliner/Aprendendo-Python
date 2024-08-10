# Aprimoramento

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma = 0

# Entrada de valores na matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a [{l}][{c}]: '))

# Exibição da matriz e cálculos
for l in range(0, 3):
    for c in range(0, 3): 
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()

# Calcula o maior valor da segunda linha
maior_valor = max(matriz[1])

# Calcula a soma dos valores da terceira coluna
for l in range(0, 3):
    soma += matriz[l][2]

print()
print(f'A soma de todos os valores pares: {pares}')
print(f'A soma de todos os valores da 3ª coluna é: {soma}')
print(f'O maior valor da segunda linha: {maior_valor}')




# Minha forma de calculo...

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# pares = 0
# soma = 0
# maior_valor = 0

# for l in range(0, 3):
#     for c in range(0, 3):

#         matriz[l][c] = int(input(f'Digite o valor para a [{l}][{c}]: '))

# for l in range(0, 3):
#     for c in range(0,3):

#         print(f'[{matriz[l][c]:^5}]',end='')
#         if matriz[1][-1] > matriz[1][0]:
#             maior_valor = matriz[1][c]
#         elif matriz[1][-1] < matriz[1][1]:
#             maior_valor=matriz[1][1]
#         else:
#             maior_valor = matriz[1][0]

#         if matriz[l][c] % 2 == 0:
#             pares += matriz[l][c]
#     print()

# for l in range(0,3):    
#     for c in range(0, 1):
#         soma += matriz[l][2]



# print()
# print(f'A soma de todos os valores pares: {pares}')
# print(f'A soma de todos os valores da 3ª coluna é: {soma}')
# print(f'O maior valor da segunda linha: {maior_valor}')