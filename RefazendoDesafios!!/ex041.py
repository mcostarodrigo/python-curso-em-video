from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Clasificação: \033[1:32mMIRIM')
elif 10 <= idade <= 14:
    print('Classificação: \033[1:32mINFANTIL ')
elif 14 <= idade <= 19:
    print('Classificação: \033[1:32mJÚNIOR')
elif 19 <= idade <= 25:
    print('Classificação: \033[1:32mSÊNIOR')
else:
    print('Classificação: \033[1:32mMASTER')