# #Minha versão do codigo

from random import randint
from time import sleep

# num_sort = []

# def sorteia():
#     for c in range(0, 5):
#         sort = randint(1, 10)
#         num_sort.append(sort)
#     print(f'Sorteando 5 valores da lista: ', end='')
#     for valor in num_sort:
#         print(f'{valor} ', end='', flush=True)
#         sleep(0.2)
#     print()
# def somaPar():
#     soma = 0
#     for valor in num_sort:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'Somando os valores pares de {num_sort}, temos {soma}')

# #Programa principal
# sorteia()
# somaPar()


# Versão do guanabara
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
    
numeros = []
sorteia(numeros)
somaPar(numeros)