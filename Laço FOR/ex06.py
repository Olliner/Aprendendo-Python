
# Inicializa a soma
soma = 0

# Loop de 1 a 500
for c in range(1, 500+1):
    # Verifica se o número é ímpar e múltiplo de 3
    if c % 2 != 0 and c % 3 == 0:
        soma += c

# Imprime o resultado
print(soma)
