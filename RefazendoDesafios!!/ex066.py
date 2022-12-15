o = 's'
soma = cont = 0
while o != 'n':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    o = input('Quer continuar? [S/N] ').lower()
media = soma / cont
print(f'Você digitou {cont} números e sua média foi {media:.2f}')