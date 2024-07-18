from math import factorial

numero = int(input('Digite um numero: '))
f = factorial(numero)
c = numero
print(f'Calculando {numero}! = ')
while c > 0:
    print(f'{c}', end=' ' )
    print('x ' if c > 1 else f' = {f}', end='')
    c -= 1