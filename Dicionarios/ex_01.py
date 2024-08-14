alunos = dict()
cadastros = list()

while True:
    alunos['Nome'] = str(input('Nome: '))
    alunos['Média'] = float(input(f'Qual é a média de {alunos["Nome"]}: '))
    print('=-' * 40)
    if alunos['Média'] < 7:
        alunos['Situação'] = 'Reprovado'
    else:
        alunos['Situação'] = 'Aprovado'
    cadastros.append(alunos.copy())
    SN = str(input('Continuar[S/N]: ')).strip().upper()
    print('=-' * 40)
    if SN == 'N':
        break
print(f'{'Situação Dos alunos':^80}')
print('==' * 40)
for a in cadastros:
    for k, v in a.items():
        print(f'{k}: {v}')
    print()