from datetime import datetime
from time import sleep

formulario = list()

while True:
    dados = dict()
    dados["Nome"] = str(input('Nome: '))
    ano_nascimento = int(input('Ano de Nascimetno: '))
    ano_atual = datetime.now().year
    dados["Idade"] = ano_atual - ano_nascimento
    dados["CTPS"] = int(input('CTPS [Digite "0" caso não tenha]: '))

    if dados['CTPS'] != 0:
        dados["Ano de contratação"] = int(input('Ano de contratação: '))
        dados["Salario"] = float(input('Salario: '))
        dados["Aposentar"] = dados["Idade"] + 35
        print('--'*40)
        print()
        for k, v in dados.items():
            print(f'{k}: {v}')
            sleep(1)
        break
    else:
        print('--'*40)
        print()
        for key, value in dados.items():
            print(f'{key}: {value}')
            sleep(1)
        break
