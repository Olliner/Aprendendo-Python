from colorama import Fore, Style
from datetime import datetime

ano_atual = datetime.now().year

cancelar_cor = Style.RESET_ALL
vermelho = Fore.RED
verde = Fore.GREEN



for i in range(1, 8):
    nascimento = int(input('Ano de Nascimento: '))
    idade = ano_atual - nascimento
    if idade >= 21:
        print(verde,f'Pessoa {i} de maior. Idade: {idade}',cancelar_cor)
    else:
        print(vermelho,f'Pessoa {i} de menor. Idade: {idade}',cancelar_cor)


