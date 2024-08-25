# def maior(*num):

#     qtd = len(num)
#     print('Analisando os valores passados...')
#     if qtd == 0:
#         print(f'Foram informados {qtd} valores ao todo.')
#         print(f'O maior valor informado foi {qtd}')
#     else:
#         print(f'Foram informados {qtd} valores: {num}')
#         print(f'O maior valor foi {max(num)}')
#         print('=-' * 40)
       
# #Programa principal
# maior(2,9,4,5,7,1)
# maior(4,7,0)
# maior(1,2)
# maior(6)
# maior()
from time import sleep

def maior(*num):
    cont = maior= 0
    print('-=' * 40)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
            




maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()