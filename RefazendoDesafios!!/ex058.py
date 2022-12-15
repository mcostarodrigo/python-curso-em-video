from random import randint
x = randint(0, 9)
cont = 1
print(x)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi? ')
j = int(input('Qual é seu palpite? '))
while j != x:
    cont +=1
    if j < x:
        j = int(input('Mais...Tente mais uma vez '))
    else:
        j = int(input('Menos ...Tente mais uma vez '))
print(f'Acertou com {cont} tentativas. Parabéns!')
