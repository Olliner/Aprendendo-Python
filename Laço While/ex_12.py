print('--' * 30)
print('CADASTRO DE PESSOAS!')
print('--' * 30)
print('')

cont = 0
mais18 = 0
qtdhomens = 0
qtdmulheresmenos20 = 0

while True:

    while True:
        try:
            idade = int(input('Idade: '))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")
    
    while True:
        sexo = input('Sexo [F/M]: ').strip().upper()
        if sexo in ['F', 'M']:
            break
        else:
            print("Entrada inválida. Por favor, insira 'F' para feminino ou 'M' para masculino.")

    while True:
        desejo = input('Quer continuar [S/N]: ').strip().upper()
        print('*-' * 20)
        print('')
        if desejo in ['S', 'N']:
            break
        else:
            print('Digito invalido. digite S para sim  e N para Não.')

    cont += 1

    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        qtdhomens += 1
    if idade < 20 and sexo == 'F':
        qtdmulheresmenos20 += 1

    if desejo == 'N':
        print(f'Você cadastrou {cont} pessoas.')
        print(f'Com mais de 18 anos: {mais18}')
        print(f'Quantidade de homens: {qtdhomens}')
        print(f'A quantidade de mulheres com menos de 20 anos: {qtdmulheresmenos20}')
        print('')
        print('Obrigado por cadastrá-los!')
        break
