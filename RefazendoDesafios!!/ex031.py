viagem = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {viagem:.0f}km.')
if viagem > 200:
    print(f'E o preço de sua passagem será de R${viagem*0.45:.2f}')
else:
    print(f'E o preço de sua passagem será de R${viagem*0.50:.2f}')