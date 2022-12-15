m = float(input('\033[1:37mQuanto dinheiro você tem na carteira?: R$ \033[m'))
print(f'Com \033[1:35mR${m:.2f}\033[m você pode comprar \033[1:32mUS${m / 3.27 :.2f} \033[m')