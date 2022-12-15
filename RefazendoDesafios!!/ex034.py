salario = float(input('Qual o salário do funcionário: R$'))
if salario <= 1250.00:
    aumento = salario * 1.15
else:
    aumento = salario * 1.1
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora. ')