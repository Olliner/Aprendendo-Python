print('Gerador de pa')
print('*-' *25)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} >>', end =' ')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos Termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {total} Mostrados.')