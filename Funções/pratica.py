# def soma(a, b): #Soma esta respendo dois parametros (a e b)
#     print(f'A = {a}, B = {b}')
#     s = a + b
#     print(s)


# #programa principal
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)
# # se houver apenas um paramentro como 'soma(1)' não será possivel pois a função soma somente recebe dois parametros

# #posso também dar comando especificos como:
# soma(b=4, a=5)

# def contador(*num):
#     for valor in num:
#         print(f'{valor} ', end='')
#     # ou
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números')


# contador(2, 1, 7)
# contador(8, 0)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos+=1


# valores = [6, 4, 5, 6, 7]
# dobra(valores)
# print(valores)

def soma(* valores):
    s=0
    for num in valores:
        s += num
    print(f'Somando os Valores {valores} temos {s}')


soma (5, 2)
soma (2, 9, 5)