valores = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))
print(f'Os valores digitados foram: {valores}')


print(f'O numero 9 foi digitado {valores.count(9)} vezes')

if 3 in valores:
    print(f'O valor 3 foi digitado na posição {valores.index(3) + 1}')
else:
    print('Não há nenhum 3 digitado na tupla.')


# Mais prática:
for n in valores:
    if n % 2 == 0:
        print('Os valores pares foram',n,end=' ')




# Uma das formas
# if valores[0] % 2 == 0:
#     print(f'Valores par: {valores[0]}')
# if valores[1] % 2 == 0:
#     print(f'Valores par: {valores[1]}')
# if valores[2] % 2 == 0:
#     print(f'Valores par: {valores[2]}')
# if valores[3] % 2 == 0:
#     print(f'Valores par: {valores[3]}')