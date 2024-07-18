cont = soma = 0
while True:
    numero = int(input('Digite um numero [Digite 999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A quantidade de numero digitado foi {cont} e a soma deles é {soma}')