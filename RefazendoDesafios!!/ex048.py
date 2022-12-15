contador = 0
soma = 0
for x in range(1, 500, 2):
    if x % 3 == 0:
        contador +=1
        soma = soma + x
print(f'A soma de todos os {contador}, é de {soma}')



