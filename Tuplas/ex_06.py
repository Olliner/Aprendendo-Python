palavras = ('python', 'aprender', 'desenvolver', 'programar', 'computador', 'javascript', 'software')

vogais = 'aeiou'
for palavra in palavras:
    vogais_encontradas = ''
    for letra in palavra:
        if letra in vogais:
            vogais_encontradas += letra + ' '
    print(f'Na palavra {palavra} há: {vogais_encontradas}')