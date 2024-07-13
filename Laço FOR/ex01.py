import time
fogos = '🧨'
fim = '💥'

print('Prepare-se para armar a bomba soldado 💂')
time.sleep(0.5)
print('')
print('Defina a contagem da bomba ')
print('')
print('💣  '*20)
print('')
time.sleep(0.3)
contagem = int(input('Tempo até a explosão: '))




for c in range (1, contagem+1):
    print('🧨 {}'.format(c))
    time.sleep(1)
print('{} BOOOOOOOOOOOOM!'.format(fim))
