listagem_produtos = ('Creme Dental', 10.90, 'Fio Dental', 6.60, 'Shampoo', 11.90, 'Condicionador', 12.90, 'Escova de Dentes', 10.90, 'Sabonete', 2.50, 'Lenço Umidecido', 9.90)
print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)
for pos in range(0, len(listagem_produtos)):
    if pos % 2 == 0:
        print(f'{listagem_produtos[pos]:.<30}', end='')
    else:
        print(f'R${listagem_produtos[pos]:>7.2f}')
print('-' * 40)
print('')