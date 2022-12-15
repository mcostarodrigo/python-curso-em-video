nome = input('Qual o nome de quem vamos analisar? ').title().strip()
peso = float(input('Qual é seu peso? (kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = peso / (alt * alt)
print(f'{nome} seu IMC do é de {imc:.1f} ')
if imc < 18.5:
    print(f'Você está \033[1:34mABAIXO DO PESO\033[m normal {nome}!')
elif imc < 25 > 18.5:
    print(f'\033[1:32mPARABÉNS,\033[m você está na faixa de PESO NORMAL {nome}!')
elif imc < 30 > 25:
    print(f'Você está com \033[1:35mSOBREPESO\033[m {nome}')
elif imc < 40 > 30:
    print(f'Você está \033[31mOBESO\033[m {nome}')
elif imc > 40:
    print(f'Você está em situação de \033[1:35mOBESIDADE MORBIDA\033[m {nome},cuidado!')