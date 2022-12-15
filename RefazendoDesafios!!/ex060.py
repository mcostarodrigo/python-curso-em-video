x = int(input('Digite um número para \ncalcular seu Fatorial: '))
resultado = 1
print(f'Calculando o {x}! = ', end=' ')
while x > 0: #Como x perde um elemento em cada rodada, ele deve parar ao chegar em 0
    resultado *=x #Essa variável acumula os valores multiplicados. 6*x=6x >> 5*x=5x ...
    if x > 1:
        print(f'{x} x', end=' ')
    else:
        print(f'{x} =', (resultado)) #Se x == 1 print "x ="
    x -=1 #A cada rodada, x perde um elemento para a visualização solicitada ser mostrada.
