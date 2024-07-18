print('--' * 20)
print('Leitor de Compras')
print('--' * 20)
print('')

cont = 0
total = 0
mais_de_1000 = 0
mais_barato = None 
nome_mais_barato = ''

while True:

    # Seção de nome do produto
    cont += 1
    while True:
        produto_nome = input('Produto: ').strip().upper()
        if not produto_nome.isalpha():
            print('Permitido somente letras. Digite novamente!')
        else:
            break

    # Seção de valor do produto
    while True:
        try:
            preco_produto = float(input('Preço: R$ '))
            if preco_produto < 0:
                print('O valor não pode ser negativo! Tente novamente.')
            else:
                break
        except ValueError:
            print('Por favor, insira um número válido para o preço.')

    total += preco_produto

    if preco_produto > 1000:
        mais_de_1000 += 1

   
    if mais_barato is None or preco_produto < mais_barato:
        mais_barato = preco_produto
        nome_mais_barato = produto_nome

    # Seção de encerramento
    while True:
        desejo = input('Deseja continuar [S/N]: ').strip().upper()
        if desejo in ['S', 'N']:
            break
        else:
            print('Dígito inválido. Digite S [sim] ou N [não]')

    if desejo == 'N':
        print('')
        print('Todos os produtos foram cadastrados!')
        print('*-*' * 20)
        print('')
        break
    
    print('*-' * 20)
    print('')

print(f'Foram cadastrados {cont} produtos.')
print(f'O total deles é: R${total:.2f}')
print(f'A quantidade de produtos de mais de R$1.000,00 é {mais_de_1000}')
if mais_barato is not None:
    print(f'O produto mais barato foi {nome_mais_barato} custando R${mais_barato:.2f}')
else:
    print('Nenhum produto foi cadastrado.')
