city = str(input('Em que cidade você nasceu? ')).strip().lower()
n = (city.count('santo', 0, 5))
if n == 0:
    print('False')
else:
    print('True')


