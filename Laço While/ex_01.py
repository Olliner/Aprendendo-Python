sexo = str(input('Informe seu sexo(F/M): ')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input('Dados invalidos porfavor informe seu sexo: '))
print(f'Sexo {sexo} Registrado com sucesso!')