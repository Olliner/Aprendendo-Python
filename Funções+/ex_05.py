# def notas(*args,sit=True):
#     boletim = dict()
#     boletim['Total'] = len(args)
#     boletim['Maior'] = max(args)
#     boletim['Menor'] = min(args)
#     boletim['Média'] = sum(args) / len(args)

#     if sit:
#         if boletim['Média'] >= 7:
#             boletim['Situação'] = 'BOA'
#         elif 5 <= boletim['Média'] < 7:
#             boletim['Situação'] = 'Rázoavel'
#         else:
#             boletim['Situação'] = 'Ruim'

#     return boletim



# resp = notas(5.5, 2.5, 1.5, sit=True)
# print(resp)

def notas(*args, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    args: uma ou mais notas dos alunos(aceita varias)
    sit: Valor opcional. indicando se deve ou ão adicionar a situação
    return: dicionario com várias informações sobre a situação de turma

    """
    boletim = dict()
    maior = args[0]
    menor = args[0]
    soma = 0

    for n in args:
        soma += n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
    boletim['total'] = len(args)
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['media'] = soma / len(args)
    if sit:
        if boletim['media'] >= 7:
            boletim['situação'] = 'Boa'
        elif 5 <= boletim['media'] < 7:
            boletim['situação'] = 'Razoavel'
        else:
            boletim['situação'] = 'Ruim'
    
    return boletim

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
help(notas)