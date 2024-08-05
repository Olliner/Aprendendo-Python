valores = []

for v in range(0, 5):
    valor = int(input('Digite um valor: '))

    if not valores:
        print('Valor adicionado na posição zero...')
        valores.insert(0, valor)
    elif valor > valores[-1]:
        print('Valor adicionado na última posição...')
        valores.append(valor)
    else:
        inserido = False
        for i in range(len(valores)):
            if valor <= valores[i]:
                print(f'Valor adicionado na posição {i}...')
                valores.insert(i, valor)
                inserido = True
                break
        if not inserido:
            print('Valor adicionado na última posição...')
            valores.append(valor)

print(valores)
