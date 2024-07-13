import random
import time

computador = random.randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?  '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('menos... Tente mais uma vez.')
        elif jogador < computador:
            print('mais... Tente mais uma vez.')
print(f'Acertou! com {palpite} tentativas.')
