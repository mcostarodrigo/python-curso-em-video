from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO !!!')
sleep(0.5)
print(11 * '-=')
print(f'O computador jogou {itens[computador]}') #O computador jogou {itens na posição [computador]}
print(f'O jogador jogou {itens[jogador]}') #o jogador jogou {itens na posição [jogador]}
print(11 * '-=')
if computador == 0:  #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!!')
    elif jogador ==2:
        print('COMPUTADOR VENCE!!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  #Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  #Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE!!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
