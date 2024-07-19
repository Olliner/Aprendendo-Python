from colorama import Fore, Style
import time

# Definindo cores
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Style.RESET_ALL

# Cabeçalho do caixa eletrônico
print(f'{green}--' * 30)
print('------------------ CAIXA ELETRÔNICO ------------------')
print('--' * 30)
print('')

# Variáveis iniciais
cedulas = [50, 20, 10, 1]
nome = ''

# Validação do nome
while not nome.strip() or not all(char.isalpha() or char.isspace() for char in nome):
    nome = input('Digite seu nome: ').strip()
    if not nome:
        print(f'{red}É necessário digitar seu nome.{reset}')
    elif not all(char.isalpha() or char.isspace() for char in nome):
        print(f'{red}Digite um nome válido (apenas letras e espaços são permitidos).{reset}')
    
print(f'{green}Olá {reset}{nome}!')

# Solicitação do valor de saque
while True:
    try:
        valor = int(input(f'{green}Informe o valor a ser sacado: {reset}'))
        if valor <= 0:
            raise ValueError
        break
    except ValueError:
        print(f'{red}Por favor, insira um valor inteiro positivo.{reset}')

# Processamento das cédulas
print(f'\n{blue}Contagem das cédulas:{reset}')
for ced in cedulas:
    total_cedula = 0
    while valor >= ced:
        valor -= ced
        total_cedula += 1
    if total_cedula > 0:
        print(f'Total de {total_cedula} cédulas de R$ {ced}')

print(f'\n{green}Saque concluído!{reset}')
