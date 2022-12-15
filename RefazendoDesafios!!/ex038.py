num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
if num1 > num2:
    print(f'O número {num1:.0f} é maior que o {num2:.0f}')
elif num2 > num1:
    print(f'O número {num2:.0f} é maior que o {num1:.0f}')
else:
    print('Os números são iguais')