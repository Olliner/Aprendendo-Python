def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
    return f

num = int(input('Número: '))

while True:
    mostrar = input('Deseja mostrar o cálculo [S/n]: ').strip().upper()
    if mostrar in ['S', 'N']:
        break
    print('Entrada invalida!')
if mostrar == 'S':
    mostrar = True
else:
    mostrar = False

print(fatorial(num, mostrar))
