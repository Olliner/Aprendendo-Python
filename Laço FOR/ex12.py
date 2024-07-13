# Exercício Python 56: Desenvolva um programa que leia o nome, 
# idade e sexo de 4 pessoas. No final do programa, mostre: 
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from colorama import Fore, Style

vermelho = Fore.RED
verde = Fore.GREEN
azul = Fore.BLUE

cancelar_cor = Style.RESET_ALL

soma_idade = 0
mais_velho = ''
maior_idade = 0
menos_vinte = 0

for p in range(1, 5):
    print(f'------------ {p}ª Pessoa ----------------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(f/m): ').lower())
    # Media
    soma_idade += idade
    
    # Homem mais velho
    if sexo == 'm':
        if idade > maior_idade:
            maior_idade = idade
            mais_velho = nome
    # Mulheres com menos de 20  
    if sexo == 'f':
        if idade < 20:
            menos_vinte += 1

media = soma_idade / p

print('+-' * 30)
print('')
print(f'A idade média do grupo das {p} pessoas é: {vermelho}{media}', cancelar_cor)
print(f'O nome do homem mais velho é: {verde}{mais_velho}', cancelar_cor)
print(f'A quantidade mulheres com menos de 20 anos é: {azul}{menos_vinte} ', cancelar_cor)