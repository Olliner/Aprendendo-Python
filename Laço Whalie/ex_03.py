opcao = 0
while opcao != 5:
    valor_1 = int(input('Primeiro Valor: '))
    valor_2 = int(input('Segundo Valor: '))
    while opcao != 5:
        print('Digite: \n[1] Soma\n[2] Maior\n[3] Multiplicação\n[4] novos numeros\n[5] Sair do programa')
        opcao = int(input('Digite a opção: '))
        print('')
        if opcao == 1:
            soma = valor_1 + valor_2
            print('')
            print(f'{valor_1} + {valor_2} = {soma}')
        elif opcao == 2:
            if valor_1 > valor_2:
                print(f'O Maior valor é {valor_1}')
            elif valor_1 == valor_2:
                print(f'Ambos são iguas')
            else:
                print(f'O maior valor é {valor_2}')
        elif opcao == 3:
            multiplicao = valor_1 * valor_2
            print('')
            print(f'{valor_1} x {valor_2} = {multiplicao}')
        elif opcao == 4:
            break
        else:
            print('Oção Invalida!')
            print('')
