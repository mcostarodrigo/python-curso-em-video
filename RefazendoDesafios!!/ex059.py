from time import sleep
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
op = 0
sleep(0.5)
while op != 5:
    op = int(input('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ]sair do programa\n>>>>> Qual é sua opção: '))
    sleep(0.5)
    if op == 1:
        print(f'{x} + {y} = {x + y}')
        print(20 * '=')
        sleep(0.5)
    if op == 2:
        print(f'{x} x {y} = {x * y}')
        print(20 * '=')
        sleep(0.5)
    if op == 3:
        if x > y:
            print(f'O primero valor {x} é o maior entre os dois.')
            print(20 * '=')
            sleep(0.5)
        else:
            print(f'O valor {y} é o maior entre os dois. ')
            print(20 * '=')
            sleep(0.5)
    if op == 4:
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))
        op = 0
        sleep(0.5)
    if op == 5:
        print('Finalizando...')
        sleep(0.5)
        print('Fim do programa, volte sempre!!')
        break
    if op not in [1,2,3,4,5]:
        print('Por favor, digite um valor válido.')
        sleep(0.5)


