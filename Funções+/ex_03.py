# def ficha(n=0, g=0):
#      print(f'O jogador {n} fez {g} Gol(s) no campeonato.')


# nome = str(input('Nome do jogador: '))
# if not nome:
#      nome = '<Desconhecido>'
# gols = str(input('Numero de gols: '))
# if not gols:
#      gols = 0
# ficha(nome, gols)

def ficha(jog='<Desconhecido>', gol=0):
    print(f'O Jogador {jog} fez  {gol} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g= int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
