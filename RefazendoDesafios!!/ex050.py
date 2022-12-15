soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        soma = soma + n
print(f'Você informou {cont}, números pares, e a soma deles foi {soma}')
print(len(soma))