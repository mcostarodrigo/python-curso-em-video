n = c = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {c}, e a soma entre eles foi {soma}')
