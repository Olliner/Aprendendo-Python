from colorama import Fore, Style


cancelar_cor = Style.RESET_ALL
vermelho = Fore.RED
verde = Fore.GREEN


maior = 0
menor = 0

for p in range(1, 6):
    peso_pessoa = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso_pessoa
        menor = peso_pessoa
    else:
        if peso_pessoa > maior:
            maior = peso_pessoa
        if peso_pessoa < menor:
            menor = peso_pessoa
print(vermelho, f'O menor peso lido foi {menor}', cancelar_cor)
print(verde, f'O maior peso lido foi {maior}', cancelar_cor)