Pessoas_cadastradas = list()
dados = list()
qtdpessoas = 0
pesadas = list()
leves = list()

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    Pessoas_cadastradas.append(dados[:])
    dados.clear()
    qtdpessoas += 1

    pergunta = str(input('Deseja continuar [S/N]: ')).strip().lower()
    if pergunta == 'n':
        break

# Classificação das pessoas pesadas e leves
pesadas.clear()
leves.clear()
for p in Pessoas_cadastradas:
    if p[1] > 100:
        pesadas.append(p[0])
    else:
        leves.append(p[0])

print('')
print('*-' * 40)
print(f'A quantidade de pessoas cadastradas foi {qtdpessoas}!')
print(f'Pessoas pesadas (peso > 100): {pesadas}')
print(f'Pessoas leves (peso <= 100): {leves}')
