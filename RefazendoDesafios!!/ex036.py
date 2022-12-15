casa = float(input('Valor da casa: R$'))
salario = float(input('Qual o salário do comprador: R$'))
tempo = float(input('Quantos anos de financiamento? '))
prestacao = casa / (tempo * 12)
if 0.30 * salario < prestacao:
    print(f'Para pagar uma casa de R${casa:.2f} em {tempo:.0f} anos a prestação será de R${prestacao:.2f}.\nEmpréstimo NEGADO!')
else:
    print(f'Para pagar uma case de R${casa:.2f} em {tempo:.0f} anos a prestação será de R${prestacao:.2f}.\nEmpréstimo CONCEDIDO!')