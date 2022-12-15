cont = 0
x = int(input('Digite um número para ver sua tabuada: '))
for n in range(1, 10):
    cont += 1
    print(f'{cont} x {x} = {cont * x}')