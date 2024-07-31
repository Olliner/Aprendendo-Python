import random


nA1 = random.randint(1, 10)
nA2 = random.randint(1, 10)
nA3 = random.randint(1, 10)
nA4 = random.randint(1, 10)
nA5 = random.randint(1, 10)

lista_numeros = nA1, nA2, nA3, nA4, nA5

print('*-' * 30)
print(f'Os numeros sorteados foram: {lista_numeros}')
print('*-' * 30)
print('')

maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)

print(f'O maior valor é: {maior_valor}')
print(f'O menor valor é: {menor_valor}')