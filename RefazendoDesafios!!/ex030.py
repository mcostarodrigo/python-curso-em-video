num = int(input('\33[1:35mMe diga um número qualquer \33[m'))
if num % 2 == 0:
    print(f'\33[1:37mO número {num} é \33[1:34mPAR')
else:
    print(f'\33[1:37mO número {num} é IMPAR')