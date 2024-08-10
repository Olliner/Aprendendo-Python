print('*-' * 40)
print(f'{'CADASTRO DE NOTAS':^80}')
print('*-' * 40)


alunos_cadastrados = list()

while True:
    dados = list()
    nome = str(input('Nome: '))
    n1 = float(input('1ª Nota: '))
    n2 = float(input('2ª Nota: '))
    media = (n1 + n2) / 2
    dados.append(nome)
    dados.append(n1)
    dados.append(n2)
    dados.append(media)

    alunos_cadastrados.append(dados[:])

    desejo = str(input('Deseja cadastrar mais alunos [S/N]: ')).strip().upper()
    print('=-' * 40)

    if desejo == 'N':
        print(f'{'No.':<15}{'Nome':^15}{'Média':>15}')
        print('--' * 40)
        for i, aluno in enumerate(alunos_cadastrados):
            print(f'{i:<15}{aluno[0]:^15}{aluno[3]:>15}')
        break
print('__'*40)

while True:
    ntse = int(input('Digite o Numero do aluno que deseja ver as notas[999 encerra]: '))
    if ntse != 999:
        for i, aluno in enumerate(alunos_cadastrados):
            if ntse == i:
                print(f'Notas do(a) {aluno[0]}: {aluno[1:3]}')
                print('__'*40)
    else:
        break

    
    
   