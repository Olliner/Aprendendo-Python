print('='* 20)
print('10 TERMOS DE UMA PA')
print('='* 20)


termo1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = termo1 + (10 - 1) * r

for i in range(termo1, decimo + r, r ):
    print(f'{i}  ', end='➔  ')
print('Acabou!')