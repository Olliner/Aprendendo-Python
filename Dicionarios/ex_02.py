from random import randint
from time import sleep

# armz = []
# valores_usados = set()  

# for c in range(1, 4 + 1):
#     dados = {}
#     dados["Nome"] = str(input(f'Nome jogador [{c}]: '))
    
#     while True:
#         valor = randint(0, 6)
#         if valor not in valores_usados:
#             valores_usados.add(valor)
#             dados["Dados"] = valor
#             break
    
    
#     armz.append(dados)

# armz.sort(key=lambda x: x["Dados"], reverse=True)

# cont = 1
# for j in armz:
#     nome = j["Nome"]
#     valor_dados = j["Dados"]
#     print(f'{cont}ª Lugar: {nome} com o valor {valor_dados}')
#     sleep(1)
#     cont += 1
from random import randint
from time import sleep

print('Valores sorteados')
print('*-' * 40)

valor_armazenado = set()
jogadores = []


for c in range(1, 4 + 1):
    dados = dict()
    
    while True:
        valor = randint(1, 6)
        if valor not in valor_armazenado:
            valor_armazenado.add(valor)
            dados["Dado"] = valor
            break
    
    jogadores.append({"Jogador": c, "Dado": dados["Dado"]})
    

    print(f'O Jogador {c} Tirou {dados["Dado"]}')
    sleep(1)


ordenado = sorted(jogadores, key=lambda x: x["Dado"], reverse=True)


print('\nResultado final:')
print('*-' * 40)
for posicao, jogador in enumerate(ordenado, start=1):
    print(f'{posicao}ª Colocado: Jogador {jogador["Jogador"]} com o dado {jogador["Dado"]}')
    sleep(1)
