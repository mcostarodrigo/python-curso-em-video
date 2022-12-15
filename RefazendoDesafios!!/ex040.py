n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2} a média do aluno é {media}')
if media >= 7:
    print('O aluno está \033[1:32mAPROVADO!')
elif 5 <= media <= 6.9:
    print('O aluno está de \033[1:37mRECUPERAÇÃO!')
else:
    print('O aluno foi \033[1:31mREPROVADO!')