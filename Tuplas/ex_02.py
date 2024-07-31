times = 'Internacional', 'Bahia', 'Cruzeiro', 'Botafogo', 'Vitória', 'Palmeiras', 'Fluminense', 'Red Bull Bragantino','Vasco', 'Grêmio', 'Corinthians', 'Atlético-MG', 'São Paulo', 'Fortaleza', 'Athletico-PR', 'Cuiabá', 'Chapecoense', 'Flamengo', 'Ponte preta', 'Bangu'


print(f'Lista de times: {times}')

print('=-' * 20)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('=-' * 20)


print('=-' * 20)
print(f'Os 4 ultimos são: {times[-4:]}')
print('=-' * 20)

print('=-' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=-' * 20)


print('=-' * 20)
print(f'O Chapeconse está na posição: {times.index('Chapecoense')+1}ª')
print('=-' * 20)

