ex = str(input('Digite uma expressão: '))

armazen = []

for caracter in ex:
    if caracter == '(':
        armazen.append(caracter)
    elif caracter == ')':
        if not armazen:
            break
        armazen.pop()
else:
    if not armazen:
        print('Sua expressão está correta.')
    else:
        print('Expressão incorreta!')
