valores = list()

for c in range(0, 5): 
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

print('Você digitou os seguintes valores: ', end='')
for n in valores:
    print(f'{n} ', end='')

maior_numero = valores[0]
menor_numero = valores[0]

for valor in valores:
    if valor > maior_numero:
        maior_numero = valor
    if valor < menor_numero:
        menor_numero = valor

pos_maior = valores.index(maior_numero)
pos_menor = valores.index(menor_numero)

print(f'\nO maior valor é {maior_numero} e sua posição é: {pos_maior}!')
print(f'O menor valor é {menor_numero} e sua posição é: {pos_menor}!')
