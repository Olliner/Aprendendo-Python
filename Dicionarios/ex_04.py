
dados = dict()

dados["Nome"] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

part_list = list()
for p in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {p}: '))
    part_list.append(gols)
print('=-' * 40)
dados["Gols"] = part_list
dados["Total"] = sum(part_list)

for k, v in dados.items():
    print(f'{k}: {v}')
print('-=' * 40)
print()

print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')

for i, p in enumerate(part_list):
    print(f'=> Na partifa {i}, Fez {p} gols.')
print(f'Foi um total de {dados["Total"]} Gols')


