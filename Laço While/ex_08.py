cont = 0
soma = 0
maior = None
menor = None

while True:
    numero = int(input('Digite um valor: '))
    opcao = input('Deseja continuar [S/N]: ').strip().lower()
    cont += 1
    soma += numero

    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    if opcao == 'n':
        media = soma / cont
        print(f'A quantidade de termos digitada foi {cont} e a média entre eles é {media:.2f}.')
        print(f'O maior número é {maior} e o menor número é {menor}.')
        break
    elif opcao != 's':
        print('Opção inválida! Digite S ou N.')
