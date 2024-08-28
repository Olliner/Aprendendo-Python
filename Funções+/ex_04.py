from colorama import Fore, Style

def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print(f'{Fore.RED}Erro! Digite um número inteiro válido.{Style.RESET_ALL}')


n = leiaint('Digite um numero: ')
print(f'{Fore.GREEN}Você acabou de digitar o número {n}')