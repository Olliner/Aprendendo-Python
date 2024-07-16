print('*-' * 20)
print('Sequencia Fibonacci')
print('*-' * 20)
numero = int(input('Quantos termos você quer mostrar: '))
a, b = 0, 1
count = 0
if numero <= 0:
    print("Por favor, insira um número inteiro positivo.")
elif numero == 1:
    print("Sequência Fibonacci até", numero, ":")
    print(a)
else:
    print("Sequência Fibonacci:")
    while count < numero:
        print(a, end=' -> ')
        c = a + b
        a = b
        b = c
        count += 1
print('fim!')
