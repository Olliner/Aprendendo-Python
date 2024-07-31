contagem = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'



while True:
    numero_user = int(input('Digite um número entre 0 e 20: '))

    if 0 <= numero_user <= 20:
        print(f'Você digitou o número: {contagem[numero_user]}')
        desejo = str(input('Deseja continuar [S/N]: ')).strip().upper()
        
            
        if desejo == 'N':
            break
        elif desejo != 'S' and 'N':
            print('Tente novamente.', end='')

    print('Tente novamente.', end=' ')
            

