n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
if n1 < n2 and n1 < n3:
    print(f'O menor valor digitado foi {n1:.0f}')
if n2 < n1 and n2 < n3:
    print(f'O menor número digitado foi {n2:.0f}')
if n3 < n2 and n3 < n1:
    print(f'O menor valor digitado foi {n3:.0f}')
if n1 > n2 and n1 > n3:
    print(f'O maior valor digitado foi {n1:.0f}')
if n2 > n1 and n2 > n3:
    print(f'O maior valor digitado é {n2:.0f}')
if n3 > n2 and n2 < n1:
    print(f'O maior valor digitado foi {n3:.0f}')
