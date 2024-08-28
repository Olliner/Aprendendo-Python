# Interactive Help

# help()
# help(print)
#a função help explica o que cada ação faz, print, imput

#Docstring

#são feitos para orientar o próximo programador que utilizar sua função onde tera um comentario escrito o que cada função faz ele é feito com apas triplas
# def contador (i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: inicío da contagem
#     :param f : fim da contagem
#     :param p: Passo da contagem
#     :return: sem retorno

#     """
#     c = i 
#     while c <= f:
#         print(f'{c}', end=' ')
#         c += p
#     print('FIM!')
# help(contador)

# Parametros opcionais

# Caso os parametros das funções não sejam passados por completo eles recebem 0 como descrito na função a baixo
# def somar(a=0,b=0,c=0):
#     """
#     Faz a soma de 3 valores e mostra o resultado na tela.
#     a: primeiro valor
#     b: Segundo valor
#     c: terceiro valor
#     a = b = c são valores opcionais
#     """
#     s= a + b + c
#     print(f'A soma vale {s}')
# somar(3, 2, 5)
# somar(8, 4)
# help(somar)

# escopo de variáveis
# def teste():

#     x=8 #Variavel local
#     print(f'Na função n vale {n}')
#     print(f'Na função x vale {x}')

# # programa principal
# n = 2 #Variavel global
# print(f'No programa principal n vale {n}')
# teste()
# print(f'NO programa principal o x vale {x}') 

# Retorno de valores
# A função return permite que a personalização de variaveis locais como demosntrado abaixo
# def somar (a=0,b=0,c=0):
#     s = a+b+c
#     return s


# r1 = somar(3,2,5)
# r2 = somar(1,7)
# r3 = somar(4)

# print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
