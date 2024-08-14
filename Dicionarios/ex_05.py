pessoas = list()
idade = list()
mulheres = list()
acima = list()
while True:
    dados = dict()
    dados["Nome"] = str(input('Nome: '))
    dados["Sexo"] = str(input('Sexo [F/M]: ')).strip().upper()
    dados["Idade"] = int(input('Idade: '))

    idade.append(dados['Idade'])
    pessoas.append(dados)
    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])

    desejo = str(input('Deseja continuar [S/N]: ')).strip().upper()
    print('*-' * 40)
    print()
    
    if desejo == 'N':
        break

media = sum(idade) / len(pessoas)

print('=-' * 40)

print(f'Quantidade de pessoas Cadastradas: {len(pessoas)}')
print(f'A média de idade do grupo cadastrado: {media} ')
print(f'Lista de mulheres: {mulheres}')
for p in pessoas:
    if p['Idade'] > media:
        acima.append(p['Nome'])
print(f'Pessoas acima da média: {acima}')
