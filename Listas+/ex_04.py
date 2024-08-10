from random import randint
from time import sleep

print('*-' * 40)
print(f'{"JOGO DA SORTE":^80}')
print('*-' * 40)

jogos = list()

escolha = int(input('Digite a quantidade de jogos: '))

for _ in range(escolha):
    qtdjogos = list()
    while len(qtdjogos) < 6:
        numeros = randint(1, 60)
        if numeros not in qtdjogos:
            qtdjogos.append(numeros)
        qtdjogos.sort()

    if qtdjogos not in jogos:
        jogos.append(qtdjogos)

for index, jogo in enumerate(jogos):
    print(f'Jogo {index+1}: {jogo} ')
    sleep(1)

print('*-' * 40)
print(f'{"BOA SORTER":^80}')
print('*-' * 40)