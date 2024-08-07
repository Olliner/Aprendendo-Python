# teste = list()
# teste.append('Daniel')
# teste.append(23)
# galera = list()
# galera.append(teste[:]) #Através do [:] é possivel fazer uma copia e guardala na lista galera sem fazer uma alteração global
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# Para cada pessoa na lista galera sera imprimido na tela todos que estão na posição 0
# for p in galera:
#     print(f'{p[0]} tem {p[1]} de idade')

galera = list()
dado = list()
totaldemaior = totaldemenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totaldemaior += 1
    else:
        totaldemenor += 1
        print(f'{p[0]} é menor de idade')
print(f'Temos {totaldemaior} maiores e {totaldemenor} menores de idade')