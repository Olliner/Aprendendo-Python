lista = []

contador = 0
while True:
    valor = int(input('Digite um valor [0 Para encerrar] -> '))
    lista.append(valor)
    contador += 1
    if valor == 5:
         print('O digito 5 foi colocado na lista!')
    
    if valor == 0:
        lista.pop()
        contador -= 1
        print('*-' * 40)
        print(f'Quantidade de valores digitados {contador}')
        print('encerrado!')
        break

for c, valor in enumerate(lista):
    if valor == 5:
        print(f'Valor 5 encontrado na posição {c}')
        
if 5 not in lista:
    print('O valor 5 não esta na lista')

lista.sort(reverse=True)
print(lista)