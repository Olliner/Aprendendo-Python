valores = list()

while True:
    valor = int(input('Digite um valor: '))
    
    if valor in valores:
        print('Valor duplicado! Valor não adiconado...')
    else:
        print('Valor adicionado com sucesso!')
        valores.append(valor)
    
    desejo = str(input('Deseja continuar [S/N]: ')).strip().upper()

    if desejo == 'N':
        valores.sort()
        print(f'Lista de valores digitados: {valores}')
        break

        
        

    