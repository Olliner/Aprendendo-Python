from random import randint

print('*-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('*-' * 30)
print('')

cont = 0

while True:
    valor = int(input('Digite um valor: '))
    opcao = str(input('Par ou Impar? [P/I] ')).strip().upper()
    print('--' * 30)
    print('')

    escolha_maquina = randint(1, 10)
    resultado = valor + escolha_maquina
    resultado2 = 'Par' if resultado % 2 == 0 else 'Impar'

    cont += 1

    print(f'Você colocou {valor} e eu coloquei {escolha_maquina}, totalizando {resultado}, que é {resultado2}')
    print('')

    if (opcao == 'P' and resultado2 == 'Par') or (opcao == 'I' and resultado2 == 'Impar'):
        print('Você Ganhou!')
        print('*-' * 30)
        print('')
    else:
        print('Você Perdeu!')
        print('')
        print(f'Game Over! Você venceu {cont - 1} veze(s)')
        break
    print('Vamos jogar novamente...')