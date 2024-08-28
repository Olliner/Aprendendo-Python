
def voto(i):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - i
    print(f'Possui {idade} Anos!')
    if idade < 16:
        return 'Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigatório'


#programa principal
ano_nascimento = int(input('Ano de nascimento: '))
retorno = voto(ano_nascimento)
print(f'{retorno}')