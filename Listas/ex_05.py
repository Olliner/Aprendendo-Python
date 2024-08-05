valores = []

while True:
    valor = int(input('Digite um valor [digite um número negativo para encerrar]: '))
    if valor < 0:
        break
    if valor in valores:
        print('Valor já digitado! Digite outro...')
    else:
        valores.append(valor)


lista_par = []
lista_impar = []

for val in valores:
    if val % 2 == 0:
        lista_par.append(val)
    else:
        lista_impar.append(val)

print('')
print('*-' * 40)
print(f'Lista principal: {valores}')
print(f'Lista somente com os pares digitados: {lista_par}')
print(f'Lista somente com os impares digitados: {lista_impar}')