from colorama import Fore, Style

c = (Style.RESET_ALL, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.BLACK, Fore.WHITE)


def ajuda(com):
    print(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')


# Progrsma principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('Até logo', 1)
        break
    else:
        ajuda(comando)
    