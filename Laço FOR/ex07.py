
passo = 2
fim = int(input('Até que numero você quer saber se é par: '))

for c in range(0 ,fim , passo ):
    if c % 2 == 0:
        print(c)
if fim % 2 == 0:
       print(fim)
