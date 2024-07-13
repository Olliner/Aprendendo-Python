# print('Tabuada simples')
# print('*-' *25)
# print('')

# numero = int(input('Número: '))

# for c in range(1, 10+1):
#     mult = numero * c
#     print('{} * {} = {}'.format(numero, c, mult))
# print('Fim!')

print('Tabuada simples')
print('*-' * 25)
print('')

numero = int(input('Digite um número: '))

for c in range(1, 10 + 1):
    mult = numero * c
    print(f'{numero} * {c} = {mult}')

print('Fim!')
