vel = int(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('\33[1:31m MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'\33[1:31m Você deve pagar uma multa de\33[m \33[1:33mR${(vel - 80 ) * 7:.2f}! ')
print('\33[1:33mTenha um bom dia! Dirija com segurança!')
