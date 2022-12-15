print('Gerador de PA')
print('=-' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
c = 1
while c <= 10:
    print(primeiro, end=' > ')
    primeiro += razão
    c += 1
print('FIM!')
