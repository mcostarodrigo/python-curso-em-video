compra = float(input('Preços das compras: R$ '))
print('FORMA DE PAGAMENTO')
print(' [ 1 ] á vista dinheiro/cheque \n [ 2 ] á vista cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão')
ops = int(input('Qual é a opção? '))
if ops == 1:
    print(f'Sua compra de R${compra:.2F} vai custar R${compra * 0.9:.2f} no final.')
elif ops == 2:
    print(f'Sua compra de R${compra:.2f} vai custar R${compra * 0.95:.2f} no final.')
elif ops == 3:
    print(f'Sua compra será parcelada em 2x de R${compra / 2:.2f} SEM JUROS.')
    print(f'Sua compra vai custar R${compra:.2f}.')
elif ops == 4:
    parcela = int(input(f'Quantas parcelas? (Parcelamento máximo \033[1m10x\033[m)  '))
    if parcela > 10:
            print('Parcelamento máximo em até \033[1m10x\033[m. Tente novamente! ')
            quit()
    valorcomjuros = (compra * 1.2) / parcela
    print(f'Sua compra será parcelada em {parcela}x de {valorcomjuros:.2f} COM JUROS')
    print(f'Sua compra de R${compra:.2f} vai custar R${compra * 1.2:.2f} no final.')
else:
    print('Escolha uma opção sugerida.')