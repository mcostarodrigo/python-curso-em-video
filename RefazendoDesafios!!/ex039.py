from datetime import date
atual = date.today().year
sexo = int(input('''Qual seu sexo, digite:
 [ 1 ] Masculino
 [ 2 ] Feminino  
   Opção:  '''))
if sexo == 2:
    print('Você NÃO precisa se alistar!')
    quit()
else:
    ano = int(input('Ano de nascimento: '))
    idade = (atual) - ano
alistamento = idade - 18
alistamentop = 18 - idade
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if idade > 18:
    print(f'Você já deveria ter se alistado a {alistamento} anos')
    print(f'Seu alistamento foi em {(atual) - alistamento}')
elif idade < 18:
    print(f'Ainda faltam {alistamentop} anos para o alistamento')
    print(f'Seu alistamento será em {(atual) + alistamentop}')
else:
    print('Você tem que se alistar IMEDIATAMENTE.')
