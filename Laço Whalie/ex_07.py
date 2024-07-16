print('*-' * 20)
print('Leitor de numeros')
print('*-' * 20)

cont, soma, numero = 0

while numero != 999:
    numero = int(input('Digite um numero[999 para parar]: '))
    if numero != 999:
        soma += numero
        cont += 1
    elif numero == 999:
        print('Obrigado! Por participar')
        break
print(f'Foram quantificados {cont} numero e a soma deles é {soma}')
