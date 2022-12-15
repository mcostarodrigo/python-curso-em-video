from random import randint
import time
x = randint(1, 5) #Faz o computador gerar o número aleatório
y = int(input('Digite um número de 0 a 5: '))
print('Processando...')
time.sleep(3) #Faz o computador dormir por 3 segundos
if x == y:
    print(f'Você venceu, o computador pensou em {x} e você acertou!!')
else:
    print(f'O computador venceu, ele pensou no número {x} não no número {y}!')
