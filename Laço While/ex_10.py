print('--' * 20)
print('Leitor de Tabuada')
print('--' * 20)
print('')

while True:
    numero = int(input('Informe o numero para saber sua Tabuada [Qualquer numero negativo encerra o programa]: '))
    if numero < 0:
        break
        

    print(f'Tabuada do numero {numero}')

    for cont in range(1, 11):
        resultado = numero * cont
        print(f'{numero} x {cont} = {resultado}')

    print('--' * 20)
print('Obrigado!')