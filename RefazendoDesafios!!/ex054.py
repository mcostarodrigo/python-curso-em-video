from datetime import date
atual = date.today().year
seq = 0
maior = 0
menor = 0
for pessoa in range(0, 7):
    seq += 1
    pessoa = int(input(f'Em que ano a {seq}º pessoa nasceu? '))
    idade = (atual - pessoa)
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade \nE também tivemos {menor} pessoas menores de idade.')