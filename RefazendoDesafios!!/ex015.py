dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
diaria = dias * 60
dist = km * 0.15
print(f'O total a pagar é de R${diaria + dist :.2f}')