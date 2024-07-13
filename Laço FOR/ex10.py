
# soma = 0

# for c in range(1, 6+1):
#     if c % 2 == 0 and c % 3 != 0:
#         soma += c
# print(f' A soma dos números pares é: {soma}')

soma = 0

for i in range(1, 7):  # Loop para ler seis números
    num = int(input(f'Digite o {i}º número inteiro: '))
    
    if num % 2 == 0:  # Verifica se o número é par
        soma += num  # Adiciona o número par à soma

print(f'A soma dos números pares digitados é: {soma}')
