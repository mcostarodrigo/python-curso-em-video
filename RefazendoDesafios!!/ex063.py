print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
f = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print(f'{t1} > {t2}', end=' > ')
while c <= f:
    t3 = t1 + t2
    c += 1
    t1 = t2
    t2 = t3
    print(f'{t3}', end=' > ')
print('FIM', end=' ')