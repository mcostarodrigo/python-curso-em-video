num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[1:33m{c} ', end='')
        tot +=1
    else:
        print(f'\033[1:31m{c} ', end='')
print(f'\033[m\nO número {num}, foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')


