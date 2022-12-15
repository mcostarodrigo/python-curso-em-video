maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: ')) #Usei o próprio "p" como contador.
    if p == 1: #Se 'p' igual posição '1'
        maior = peso #Na primeira posição, qualquer valor digitado se torna maior.
        menor = peso #Na primeira posição qualquer valor digitado se torna menor.
    else:
        if peso > maior: #Se o peso digitado for maior que o valor salvo...
            maior = peso #Salve o valor digitado.
        if peso < menor: #Se o peso digitado for menor que o valor salvo...
            menor = peso #Salve o valor digitado.
print(f'O maior peso lido é {maior:.2f}Kg\nE o menor peso lido foi {menor:.2f}kg')
