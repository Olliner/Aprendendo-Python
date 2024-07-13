from colorama import init, Fore, Back, Style

init()

amarelo = Style.BRIGHT + Fore.YELLOW
verde = Fore.GREEN

numero = int(input('Digite um numero: '))
tot = 0
for i in range(1, numero+1):
    if numero % i == 0:
        print(amarelo, end=' ')
        tot += 1
    else:
        print(verde, end=' ')
    print(f'{i} ', end=' ')
print(f'O número {numero} foi divisivel {tot} Vezes')