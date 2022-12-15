r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmneto: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    if r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1:
            print('ISÓSCELES!')
    if r1 != r2 != r3 != r1:
        print('ESCALENO!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um trianâgulo')